# Django Docs recommend restarting server after creation
# https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/

from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, qty):
    return price * qty
