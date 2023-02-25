from django.test import TestCase
from books.models import Author, Genre, Special
from model_bakery import baker


class TestAuthor(TestCase):
    """Test Author Model"""
    def setUp(self):
        self.author = Author()
        self.author.name = "max test"
        self.author.book_title = "max book"
        self.author.about = "max book test max"
        self.author.save()

    def test_author_field_is_created(self):
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author, self.author)

    def test_author_returns_string_method(self):
        name = Author.objects.create(name=self.author.name)
        self.assertEqual(str(name), "max test")


class TestGenres(TestCase):
    """Test Author Model"""
    def setUp(self):
        self.genre = Genre()
        self.genre.name = "fantasy"
        self.genre.save()

    def test_genre_field_is_created(self):
        genre = Genre.objects.get(id=self.genre.id)
        self.assertEqual(genre, self.genre)

    def test_genre_returns_string_method(self):
        name = Genre.objects.create(name=self.genre.name)
        self.assertEqual(str(name), "fantasy")


class TestSpecial(TestCase):
    """Test Special Model"""
    def setUp(self):
        self.special = Special()
        self.special.name = "special"
        self.special.save()

    def test_special_field_is_created(self):
        special = Special.objects.get(id=self.special.id)
        self.assertEqual(special, self.special)

    def test_special_returns_string_method(self):
        name = Special.objects.create(name=self.special.name)
        self.assertEqual(str(name), "special")


class TestBooks(TestCase):
    """Test Books Model"""
    def setUp(self):
        self.book = baker.make('books.Books')

    def test_book_returns_string_method(self):
        self.assertEqual(
            str(self.book), f"{self.book.title} by {self.book.author}")
