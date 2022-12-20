from django.shortcuts import render
from checkout.forms import OrderForm


def checkout_view(request):
    """ renders order form view and
    allow users to create submit their order """

    form = OrderForm()

    context = {
        'form': form,
        'stripe_public_key': 'pk_test_51MH9dOKdGqoTwjdxLJwV8YGa2d0LjjEpYBfDGp0VPP2zxjcB4TocveeNzQeKLNUb21p3GMxyPG9vzWDN0DjT6You009oOkIW6Y',
        'client_secret': 'test client secret',
        }
    return render(request, 'checkout/checkout.html', context)
