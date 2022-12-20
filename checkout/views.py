from django.shortcuts import render
from checkout.forms import OrderForm
from cart.contexts import shopping_cart
from django.conf import settings
import stripe


def checkout_view(request):
    """ renders order form view and
    allow users to create submit their order """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})

    cart_items = shopping_cart(request)
    total = cart_items['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    form = OrderForm()

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }
    return render(request, 'checkout/checkout.html', context)
