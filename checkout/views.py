from django.shortcuts import render

# Create your views here.

def checkout_view(request):
    """ render chekout view """
    return render(request, 'checkout/checkout.html')