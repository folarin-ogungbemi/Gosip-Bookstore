from django.db import models
import uuid
from books.models import Books
from django.db.models import Sum
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator
from profiles.models import UserProfile


class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=254)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17)
    address_line_1 = models.CharField(max_length=254)
    address_line_2 = models.CharField(
        max_length=254, null=True, blank=True)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    country = CountryField(blank_label='Country')
    concluded = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    cart_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0)
    grand_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0)
    original_cart = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return str(self.order_id)

    def total_order_items(self):
        """
        updates the grand total with the total items in each order set
        """
        self.cart_total = self.cartitems.aggregate(
            Sum('set_total'))['set_total__sum'] or 0
        self.grand_total = self.cart_total
        self.save(update_fields=['cart_total', 'grand_total'])
        return self.grand_total

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        self.set_total = self.book.price * self.quantity
        super().save(*args, **kwargs)
