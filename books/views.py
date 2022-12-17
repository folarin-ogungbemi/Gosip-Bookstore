from django.shortcuts import render
from books .models import Books
from django.views.generic.list import ListView


class BookViews(ListView):
    model = Books
    template_name = "books/books.html"
    context_object_name = "books"
    paginate_by = 5
