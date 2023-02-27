from django.test import TestCase
from books.forms import AuthorForm, BookForm


# Create your tests here.
class TestAuthorForm(TestCase):

    def test_author_name_is_required(self):
        form = AuthorForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_author_book_title_is_required(self):
        form = AuthorForm({'book_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('book_title', form.errors.keys())
        self.assertEqual(
            form.errors['book_title'][0], 'This field is required.')

    def test_author_about_is_required(self):
        form = AuthorForm({'about': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('about', form.errors.keys())
        self.assertEqual(form.errors['about'][0], 'This field is required.')


class TestBookForm(TestCase):

    def test_title_is_required(self):
        form = BookForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_author_is_required(self):
        form = BookForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_genre_is_not_required(self):
        form = BookForm({'genre': ''})
        self.assertFalse(form.is_valid())
