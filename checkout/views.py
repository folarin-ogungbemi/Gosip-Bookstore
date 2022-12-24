from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from checkout.forms import OrderForm
from cart.contexts import shopping_cart
from books.models import Books
from checkout.models import OrderSet, Order
from django.conf import settings
from django.contrib import messages
import stripe


def checkout_view(request):
    """ renders order form view and
    allow users to create submit their order """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        customer_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'house_number': request.POST['house_number'],
            'street': request.POST['street'],
            'postal_address': request.POST['postal_address'],
            'city': request.POST['city'],
            'country': request.POST['country'],
        }

        # save user data in db and conclude transaction
        form = OrderForm(customer_data)
        if form.is_valid():
            order = form.save()
            for slug, qty in cart.items():
                book = get_object_or_404(Books, slug=slug)
                if isinstance(qty, int):
                    order_set = OrderSet(
                        order=order,
                        book=book,
                        quantity=qty,)
                    order_set.save()
                    Order.objects.filter(
                            order_id=str(order)).update(concluded=True)
            return redirect(reverse('home'))
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
