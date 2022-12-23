from django.db import models
import uuid
from books.models import Books
from django.db.models import Sum


class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17)
    house_number = models.CharField(max_length=10)
    street = models.CharField(
        max_length=254, blank=True)
    postal_address = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    concluded = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    cart_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0)
    grand_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0)

    class Meta:
        ordering = ['-order_id']

    def __str__(self):
        return str(self.order_id)

    @property
    def total_order_items(self):
        """
        updates the grand total with the total items in each order set
        """
        self.cart_total = self.cartitems.aggregate(
            Sum('set_total')['set_total__sum'])
        self.grand_total = self.cart_total
        self.save()


class OrderSet(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='cartitems')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    set_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        editable=False)

    def __str__(self):
        return f'{self.book.title}: {self.order.order_id}'

    def save_data(self, *args, **kwargs):
        self.set_total = self.book.price * self.quantity
        super().save(*args, **kwargs)
