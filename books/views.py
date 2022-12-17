from django.shortcuts import render
from books .models import Books
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class BookViews(ListView):
    model = Books
    template_name = "books/books.html"
    context_object_name = "books"
    paginate_by = 8


class BookDetailView(DetailView):
    model = Books
    template_name = 'books/book-details.html'
    context_object_name = 'book'
