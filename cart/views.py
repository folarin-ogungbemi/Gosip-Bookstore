from django.shortcuts import render
from cart.models import Order
from django.views.generic import ListView


class OrderView(ListView):
    """ Renders order items in cart """
    model = Order
    template_name = 'cart/shopping_cart.html'
    context_object_name = 'order_items'
