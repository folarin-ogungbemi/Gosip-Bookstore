from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    # Book View and Search Result
    path('', views.BookViews.as_view(), name='books'),
    path('result/', views.search_view, name='search-result'),
    # Author Management
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('edit_author/<id>/',
         views.update_author_view, name='edit_author'),
    path('delete_author/<id>/',
         views.delete_author, name='delete_author'),
    # Book Management
    path('edit/<slug:slug>/',
         views.update_book_view, name='edit_book'),
    path('delete/<slug:slug>/',
         views.delete_book, name='delete_book'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    # Book Details at the bottom due to slug
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book-details'),
]
