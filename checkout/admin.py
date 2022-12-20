from django.contrib import admin
from .models import Order, OrderSet


class OrderSetInline(admin.TabularInline):
    model = OrderSet


# Register your models here.
@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    inlines = [
        OrderSetInline,
    ]
    list_display = (
        'order_id', 'first_name', 'last_name', 'email', 'phone_number',
        'house_number', 'street', 'postal_address', 'city', 'country',
        'order_date', 'cart_total', 'grand_total', 'concluded')
    search_fields = ('email', 'order_id', 'country', 'order_date', 'concluded')
    list_filter = ('email', 'order_id', 'country', 'concluded')
