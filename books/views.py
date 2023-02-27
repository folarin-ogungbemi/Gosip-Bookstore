from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from books.models import Books, Genre, Special, Author

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Access security
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from .forms import BookForm, AuthorForm


class BookViews(ListView):
    model = Books
    template_name = "books/books.html"
    context_object_name = "books"
    paginate_by = 8


def search_view(request):
    """
    View that searches the Books queryset based on user input
    """

    query_set = Books.objects.all()
    query_sort = request.GET.get('sort', None)
    query_direction = request.GET.get('direction', None)
    query_specials = request.GET.get('special', None)
    query_genre = request.GET.get('genre', None)
    query_dict = request.GET.get('q', None)

    if request.GET:
        if query_sort:
            if query_sort == 'title':
                query_sort = 'lower_title'
                query_set = query_set.annotate(lower_title=Lower('title'))
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


@method_decorator(login_required, name='dispatch')
class AddAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/add_author.html'
    success_url = reverse_lazy('books:add_author')
    context_object_name = 'form'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(self.request, "Permission denied!")
            return redirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Author successfully added.")
        return redirect(reverse('books:add_book'))

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Failed to add author!. Please check the validity of the form.")
        return super().form_invalid(form)


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


@login_required
def delete_author(request, id):
    """
    Function creates ability to delete and redirects
    """
    if not request.user.is_superuser:
        messages.error(request, "sorry, Only Adminitrators allowed")
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=id)
    author.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        f'Author "{author.name}" has been successfully deleted.')
    return redirect('books:books')


@method_decorator(login_required, name='dispatch')
class AddBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'books/add_book.html'
    success_url = 'books/add_book'
    context_object_name = 'form'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(self.request, 'Permission denied!')
            return redirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Book successfully added.')
        return redirect(reverse('books:books'))

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Failed to add book!. Please check the validity of the form.")
        return super().form_invalid(form)


@login_required
def update_book_view(request, slug):
    """
    Function provides ability to edit and(or)
    update form and redirects to book-details
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only administrators are allowed.")
        return redirect(reverse('home'))

    book = get_object_or_404(Books, slug=slug)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been successfully updated.')
            return redirect(reverse('books:book-details', args=[book.slug]))
    else:
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
