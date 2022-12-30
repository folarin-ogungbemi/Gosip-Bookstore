from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfile.as_view(), name='user-profile'),
]