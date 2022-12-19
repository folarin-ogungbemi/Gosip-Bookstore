from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout_view, name='checkout'),
]
