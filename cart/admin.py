from django.contrib import admin
from .models import Order


# Register your models here.
@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'order_id', 'item', 'customer',
        'quantity', 'order_date',
        'concluded')
    search_fields = ('item', 'order_id', 'order_date', 'concluded')
    list_filter = ('item', 'order_id', 'concluded')