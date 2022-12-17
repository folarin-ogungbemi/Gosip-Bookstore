from django.contrib import admin
from books.models import Author, Special, Genre, Books

# Register your models here.
admin.site.register(Author)
admin.site.register(Special)
admin.site.register(Genre)
admin.site.register(Books)