from django.shortcuts import render


def all_books(request):
    """ render all books in store """
    return render(request, 'books/books.html')
