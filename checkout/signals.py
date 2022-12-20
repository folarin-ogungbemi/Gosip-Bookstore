from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from checkout.models import OrderSet


@receiver(post_save, sender=OrderSet)
def update_data(sender, instance, created, **kwargs):
    """
    function updates the cart total when
    cart items are either created or updated
    """
    instance.order.total_order_items()


@receiver(post_delete, sender=OrderSet)
def update_data(sender, instance, **kwargs):
    """
    function deletes the cart total when cart items are deleted
    """
    instance.order.total_order_items()
