from django import forms
from books.models import Books, Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = '__all__'
