from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookViews.as_view(), name='books'),
    path('result/', views.search_view, name='search-result'),
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('edit/<slug:slug>/',
         views.update_book_view, name='edit_book'),
    path('delete/<slug:slug>/',
         views.delete_book, name='delete_book'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book-details'),
]
