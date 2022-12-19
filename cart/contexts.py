from django.conf import settings
from decimal import Decimal


def shopping_cart(request):
    shopping_cart = []
    total = 0
    book_count = 0

    tax_deduction = total * Decimal(settings.TAX/100)

    grand_total = total

    return {
        'shopping_cart': shopping_cart,
        'total': total,
        'tax_deduction': tax_deduction,
        'book_count': book_count,
        'grand_total': grand_total,
    }
