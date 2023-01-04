from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from books .models import Books, Genre, Special
from django.views.generic.list import ListView
from django.views.generic import FormView, UpdateView
from django.views.generic.detail import DetailView
# Access security
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.db.models import Q
from django.contrib import messages
from .models import Author
from .forms import BookForm, AuthorForm


class BookViews(ListView):
    model = Books
    template_name = "books/books.html"
    context_object_name = "books"
    paginate_by = 8


def search_view(request):
    """
    function searches through the query set
    and returns result based on search
    """

    query_set = Books.objects.all()
    query_sort = request.GET.get('sort', None)
    query_direction = request.GET.get('direction', None)
    query_specials = request.GET.get('special', None)
    query_genre = request.GET.get('genre', None)
    query_dict = request.GET.get('q', None)

    if request.GET:
        if query_sort:
            if query_sort == 'x':
                query_sort = 'lower_x'
                query_set = query_set.annotate(lower_x=lower('x'))
            if query_direction:
                if query_direction == 'desc':
                    query_sort = f'-{query_sort}'
            query_set = query_set.order_by(query_sort)
        if query_specials:
            specials = query_specials.split(',')
            query_set = query_set.filter(special__name__in=specials)
            query_specials = Special.objects.filter(name__in=specials)

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

    sorting = f'{query_sort}_{query_direction}'

    context = {
            'books': query_set,
            'search_term': query_dict,
            'genre': query_genre,
            'special': query_specials,
            'sorting': sorting,
    }
    return render(request, "books/books.html", context)


class BookDetailView(DetailView):
    model = Books
    template_name = 'books/book-details.html'
    context_object_name = 'book'


class AddAuthorView(FormView):
    form_class = AuthorForm
    template_name = 'books/add_author.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "sorry, Only Adminitrators allowed")
            return redirect(reverse('home'))
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Author successfully added.')
            return HttpResponseRedirect(reverse('books:add_book'))
        else:
            messages.error(
                request,
                'failed to add author, please check the validity of the form')
            return redirect(reverse('books:add_author'))


@login_required
def update_author_view(request, id):
    """
    Function provides ability to edit and(or)
    update form and redirects to book-details
    """
    if not request.user.is_superuser:
        messages.error(request, "sorry, Only Adminitrators allowed")
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Author has been successfully updated.')
            return redirect(reverse('books:books'))
    form = AuthorForm(instance=author)
    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'books/edit_author.html', context)


class AddBookView(FormView):
    form_class = BookForm
    template_name = 'books/add_book.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "sorry, Only Adminitrators allowed")
            return redirect(reverse('home'))
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Book successfully added.')
            return HttpResponseRedirect(reverse('books:add_book'))
        else:
            messages.error(
                request,
                'failed to add book, please check the validity of the form')
            return HttpResponseRedirect(reverse('books:add_book'))


@login_required
def update_book_view(request, slug):
    """
    Function provides ability to edit and(or)
    update form and redirects to bokók-details
    """
    if not request.user.is_superuser:
        messages.error(request, "sorry, Only Adminitrators allowed")
        return redirect(reverse('home'))

    book = get_object_or_404(Books, slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Book has been successfully updated.')
            return redirect(reverse('books:book-details', args=[slug]))
    form = BookForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/edit_book.html', context)


@login_required
def delete_book(request, slug):
    """
    Function creates ability to delete and redirects
    """
    if not request.user.is_superuser:
        messages.error(request, "sorry, Only Adminitrators allowed")
        return redirect(reverse('home'))

    book = get_object_or_404(Books, slug=slug)
    book.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Book has been successfully deleted.')
    return redirect('books:books')
