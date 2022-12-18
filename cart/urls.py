from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderView.as_view(), name='shopping_cart'),
]
