from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookViews.as_view(), name='books')
]
