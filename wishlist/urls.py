from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_view, name='wishlist'),
    path('like/<slug:slug>/', views.like_book, name='wish'),
]
