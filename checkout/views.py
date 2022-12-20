from django.shortcuts import render
from checkout.forms import OrderForm


def checkout_view(request):
    """ renders order form view and
    allow users to create submit their order """

    form = OrderForm()

    context = {'form': form, }
    return render(request, 'checkout/checkout.html', context)
