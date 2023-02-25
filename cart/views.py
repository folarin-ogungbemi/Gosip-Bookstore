from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
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
        messages.add_message(
            request,
            messages.INFO,
            f'Enter a valid quantity to add "{book.title}" to cart')
        return redirect(reverse('books:book-details', args=[slug]))


def remove_book(request, slug):
    """ Returning an ordered item from the cart """
    book = Books.objects.get(slug=slug)
    try:
        cart = request.session.get('cart', {})
        cart.pop(slug)
        messages.success(
                request,
                f'"{book.title}" has been removed from your Cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as error:
        return HttpResponse(content=error, status=500)


def adjust_cart(request, slug):
    """Allow Shopper to adjust the
    quantity of items in the cart"""

    book = Books.objects.get(slug=slug)

    qty = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if qty > 0:
        cart[slug] = qty
        messages.success(
                request,
                f'You now have ({qty}) "{book.title}" in Cart ')
    else:
        cart.pop(slug)
        messages.success(
                request,
                f'"{book.title}" has been removed from your Cart')

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))
