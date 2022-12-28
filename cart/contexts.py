from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from books.models import Books


def shopping_cart(request):
    shopping_basket = []
    total = 0
    book_count = 0
    cart = request.session.get('cart', {})

    for slug, qty in cart.items():
        book = get_object_or_404(Books, slug=slug)
        total += qty * book.price
        book_count += qty
        shopping_basket.append({
            'slug': slug,
            'book': book,
            'qty': qty,
        })

    tax_deduction = total * Decimal(settings.TAX/100)

    grand_total = total

    return {
        'shopping_basket': shopping_basket,
        'total': total,
        'tax_deduction': tax_deduction,
        'book_count': book_count,
        'grand_total': grand_total,
    }
