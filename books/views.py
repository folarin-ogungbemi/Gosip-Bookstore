from django.shortcuts import render
from books .models import Books, Genre
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib import messages


class BookViews(ListView):
    model = Books
    template_name = "books/books.html"
    context_object_name = "books"
    paginate_by = 8


class BookDetailView(DetailView):
    model = Books
    template_name = 'books/book-details.html'
    context_object_name = 'book'


def search_view(request):
    """
    function searches through the query set
    and returns result based on search
    """

    query_set = Books.objects.all()
    query_genre = request.GET.get('genre', None)
    query_dict = request.GET.get('q', None)

    if request.GET:
        if query_genre:
            genres = query_genre.split(',')
            query_set = query_set.filter(genre__name__in=genres)
            query_genre = Genre.objects.filter(name__in=genres)

        if query_dict:
            queries = Q(title__icontains=query_dict) | Q(
                description__icontains=query_dict)
            query_set = query_set.filter(queries)
            if query_dict is None:
                return redirect(reverse('books:books'))
    context = {
        'books': query_set,
        'search_term': query_dict,
        'genre': query_genre,
    }
    return render(request, "books/books.html", context)
