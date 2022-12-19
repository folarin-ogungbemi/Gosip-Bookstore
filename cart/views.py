from django.shortcuts import render, redirect
from cart.models import Order
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


class OrderView(ListView):
    """ Renders order items in cart """
    model = Order
    template_name = 'cart/shopping_cart.html'
    context_object_name = 'order_items'


def order_item(request, slug):
    """ Add item in quantity to cart"""

    qty = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if slug in list(cart.keys()):
        cart[slug] += qty
    else:
        cart[slug] = qty
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('shopping_cart')
