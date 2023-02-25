import os
from django.test import TestCase, Client
from django.urls import reverse
from books.models import Author, Genre, Special, Books
from django.core.files.uploadedfile import SimpleUploadedFile


class TestSearchView(TestCase):
    def setUp(self):
        self.client = Client()
        # Books Author data Category
        self.author1 = Author.objects.create(
            name='F. Scott Fitzgerald',
            book_title='The Great Gatsby', about='about scout test')
        self.author2 = Author.objects.create(
            name='Harper Lee',
            book_title='To Kill a Mockingbird', about='about harper test')
        # Books Genre data Category
        self.genre1 = Genre.objects.create(name='Fiction')
        self.genre2 = Genre.objects.create(name='Fantasy')
        # Books Special data category
        self.special1 = Special.objects.create(name='Bestseller')
        self.special2 = Special.objects.create(name='NEW')

        image_path = os.path.join(os.path.dirname(__file__), 'hero-2-c.jpg')
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_file = SimpleUploadedFile(
            'hero-2-c.jpg', image_data, content_type='image/jpg')

        self.book1 = Books.objects.create(
            title=self.author1.book_title,
            slug='the-great-gatsby',
            author=self.author1,
            genre=self.genre1,
            description='A classic novel about the Jazz Age',
            publication_year=2023,
            pages=5,
            language='english',
            isbn=12345678909,
            dimension='12x34',
            price=12.50,
            image=image_file
        )
        self.book1.special.set([self.special1])

        self.book2 = Books.objects.create(
            title=self.author2.book_title,
            slug='to-kill-a-mockingbird',
            author=self.author2,
            description='A novel about racism and injustice in the South',
            genre=self.genre2,
            publication_year=2023,
            pages=5,
            language='english',
            isbn=932145678909,
            dimension='12x34',
            price=12.50,
            image=image_file
        )
        self.book2.special.set([self.special2])
        self.search_url = reverse('books:search-result')
        self.books_url = reverse('books:books')

    def test_search_view_with_query_dict(self):
        response = self.client.get(self.search_url, {'q': 'novel'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)

    def test_search_view_sorting_with_lower_x(self):
        # Test sorting by lower_x in ascending order
        response = self.client.get(self.search_url, {'sort': 'title'})
        actual_queryset = response.context['books']
        expected_queryset = Books.objects.all().order_by('title')
        self.assertQuerysetEqual(actual_queryset, expected_queryset)

    def test_search_view_with_query_sort_and_direction(self):
        # Test sorting by lower_x in descending order
        response = self.client.get(
            self.search_url, {'sort': 'title', 'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        actual_queryset = response.context['books']
        expected_queryset = Books.objects.all()
        self.assertQuerysetEqual(actual_queryset, expected_queryset)

    def test_search_view_with_query_specials(self):
        response = self.client.get(self.search_url, {'special': 'Bestseller'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertNotContains(response, self.book2.title)

    def test_search_view_with_query_genre(self):
        response = self.client.get(self.search_url, {'genre': 'Fiction'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertNotContains(response, self.book2.title)
