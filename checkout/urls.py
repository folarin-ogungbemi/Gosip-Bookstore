from django.urls import path
from . import views
from .webhooks import my_webhook_view


urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('success/<order_id>', views.transact_success, name='successful'),
    path('wh/', my_webhook_view, name='webhook'),
]
