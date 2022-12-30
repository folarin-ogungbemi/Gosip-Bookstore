from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from checkout.forms import OrderForm
from cart.contexts import shopping_cart
from books.models import Books
from checkout.models import OrderSet, Order
from django.conf import settings
from django.contrib import messages
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout_view(request):
    """ renders order form view and
    allow users to create submit their order """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        customer_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'zip': request.POST['zip'],
            'state': request.POST['state'],
            'country': request.POST['country'],
        }

        # save user data in db and conclude transaction
        form = OrderForm(customer_data)
        if form.is_valid():
            order = form.save()
            for slug, qty in cart.items():
                try:
                    book = get_object_or_404(Books, slug=slug)
                    if isinstance(qty, int):
                        order_set = OrderSet(
                            order=order,
                            book=book,
                            quantity=qty,)
                        order_set.save()
                        Order.objects.filter(
                                order_id=str(order)).update(concluded=True)
                except book.DoesNotExist:
                    messages.error(request, (
                        "It appears a book in your cart is out of stock"
                        "Please contact us if you would like to purchase"))
                    order.delete()
            return redirect(reverse('successful', args=[order.order_id]))
        else:
            messages.error(request, "there was an error with your form \
                Please double check your information.")

    else:
        # Display Error alert when Cart is empty
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your Cart is Empty at the moment")
            return redirect(reverse('books:books'))

        cart_items = shopping_cart(request)
        total = cart_items['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        form = OrderForm()

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }
    return render(request, 'checkout/checkout.html', context)


def transact_success(request, order_id):
    """ Handle successful transaction and delete items in cart"""

    order_items = []
    total_items = 0
    order = get_object_or_404(Order, order_id=order_id)
    messages.success(request, f"Transaction was successful! \
        Your order number is: {order_id}. A confirmation \
             email will be sent to {order.email}.")

    if 'cart' in request.session:
        cart = request.session.get('cart')
        for slug, qty in cart.items():
            book = get_object_or_404(Books, slug=slug)
            total_items += qty
            order_items.append({
                'book': book,
                'slug': slug,
                'qty': qty, })
        del request.session['cart']
    context = {
        'order': order,
        'order_items': order_items,
        'total_items': total_items
    }
    return render(request, "checkout/transact_success.html", context)
