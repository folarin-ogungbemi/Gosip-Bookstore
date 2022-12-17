from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookViews.as_view(), name='books'),
    path('<slug:slug>', views.BookDetailView.as_view(), name='book-details'),
]
