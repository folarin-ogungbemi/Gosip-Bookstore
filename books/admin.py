from django.contrib import admin
from books.models import Author, Special, Genre, Books
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Author)
class AuthorsAdmin(SummernoteModelAdmin):
    summernote_fields = ('about')


admin.site.register(Special)
admin.site.register(Genre)


@admin.register(Books)
class BooksAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
