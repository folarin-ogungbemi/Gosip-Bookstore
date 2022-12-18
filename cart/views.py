from django.shortcuts import render


def cart_view(request):
    """ A view to render the checkout page """
    return render(request, "cart/shopping_cart.html")
