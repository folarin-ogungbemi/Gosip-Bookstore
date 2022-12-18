from django.db import models
import uuid
from books.models import Books
from django.contrib.auth.models import User


class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    item = models.ForeignKey(Books, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    concluded = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order_id']

    def __str__(self):
        return str(self.order_id)
