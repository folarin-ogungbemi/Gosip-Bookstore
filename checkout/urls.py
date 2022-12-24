from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('success/<order_id>', views.transact_success, name='successful'),
]
