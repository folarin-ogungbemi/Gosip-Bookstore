from django.contrib import admin
from books.models import Author, Special, Genre, Books
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Author)
class AuthorsAdmin(SummernoteModelAdmin):
    summernote_fields = ('about')
    list_display = ('name', 'book_title')
    search_fields = ('name', 'book_title')


admin.site.register(Special)
admin.site.register(Genre)


@admin.register(Books)
class BooksAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title', 'author', 'price',
        'image', 'genre', 'publication_year')
    list_filter = ('title', 'author', 'price')
    search_fields = ('title', 'author')
