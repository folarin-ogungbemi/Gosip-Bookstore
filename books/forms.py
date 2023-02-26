from django import forms
from books.widgets import CustomClearableFileInput
from books.models import Books, Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):

    image = forms.ImageField(
            label="Image", required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Books
        fields = [
            'title', 'author', 'genre', 'special',
            'publication_year', 'pages', 'language', 'isbn', 'dimension',
            'price', 'rating', 'description', 'image_url', 'image'
            ]
