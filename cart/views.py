from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from books.models import Books


def order_view(request):
    """ Renders order items in cart """
    return render(request, 'cart/shopping_cart.html')


def order_item(request, slug):
    """ Add item in quantity to cart"""
    book = Books.objects.get(slug=slug)
    try:
        qty = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if slug in list(cart.keys()):
            cart[slug] += qty
            messages.success(
                request,
                f'"{book.title}" quantity updated to ({cart[slug]})')
        else:
            cart[slug] = qty
            messages.success(
                request,
                f'"{book.title}" added to your cart')

        request.session['cart'] = cart
        return redirect('shopping_cart')
    except ValueError:
        # return a message to user on invaild input
        messages.info(
            request,
            f'Please enter a valid quantity for "{book.title}"')
        return redirect(reverse('books:book-details', args=[slug]))


def remove_book(request, slug):
    """ Returning an ordered item from the cart """
    try:
        cart = request.session.get('cart', {})
        cart.pop(slug)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as error:
        return HttpResponse(status=500)


def adjust_cart(request, slug):
    """Allow Shopper to adjust the
    quantity of items in the cart"""

    qty = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if qty > 0:
        cart[slug] = qty
    else:
        cart.pop(slug)

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))
