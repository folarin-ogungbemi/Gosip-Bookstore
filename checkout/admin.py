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

    readonly_fields = [
        'order_id', 'email', 'order_date', 'cart_total', 'grand_total'
    ]

    list_display = (
        'order_id', 'full_name', 'email', 'phone_number',
        'address_line_1', 'address_line_2', 'zip', 'city', 'state', 'country',
        'order_date', 'cart_total', 'grand_total', 'concluded')
    search_fields = ('email', 'order_id', 'country', 'order_date', 'concluded')
    list_filter = ('email', 'order_id', 'country', 'concluded')
