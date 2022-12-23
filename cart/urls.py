from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_view, name='shopping_cart'),
    path('add/<slug:slug>', views.order_item, name='in_cart'),
    path('remove/<slug:slug>/', views.remove_book, name='remove_book'),
    path('adjust/<slug:slug>', views.adjust_cart, name='adjust_cart'),
]
