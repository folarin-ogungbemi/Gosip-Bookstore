from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='shopping_cart'),
]
