from django.db import models
import uuid


class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=17)
    house_number = models.CharField(max_length=10)
    street = models.CharField(
        max_length=254, blank=True)
    postal_address = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    concluded = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    cart_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['-order_id']

    def __str__(self):
        return str(self.order_id)
