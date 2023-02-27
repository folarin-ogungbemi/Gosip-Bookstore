from django.test import TestCase, Client
from django.urls import reverse
from books.models import Author, Books
from django.utils.text import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
# authentication
from django.contrib.auth.models import User


class TestBookView(TestCase):
    def setUp(self):

        self.client = Client()
        # create an admin superuser
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='password123',
            email='admin@example.com'
        )
        # create a non-admin user
        self.non_admin_user = User.objects.create_user(
            username='user',
            password='password',
            email='user@example.com'
        )
        self.add_book_url = reverse('books:add_book')
        self.add_author_url = reverse('books:add_author')

        self.author_data = {
            'name': 'Test Author',
            'book_title': 'test book title',
            'about': 'testing'}

        self.book_data = {
            'title': 'Test Book',
            'slug': 'test-book',
            'author': 1,
            'publication_year': 2023,
            'pages': 5,
            'language': 'english',
            'isbn': 12345678909,
            'dimension': '12x34',
            'price': 12.50,
            'description': 'Test Description'
        }
        self.author = Author.objects.create(
            name='test', book_title='book title', about='tester')
        self.book = Books.objects.create(
            title='testing',
            slug=slugify('testing'),
            author=self.author,
            publication_year=2023,
            pages=5,
            language='english',
            isbn=123321123321,
            dimension='12x34',
            price=12.50,
            description='test description',
            image=SimpleUploadedFile("book_image.jpg", b"binary_content")
        )

    def test_add_book_successfully(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a POST request to the URL
        self.client.post(self.add_author_url, self.author_data)
        response = self.client.post(self.add_book_url, self.book_data)
        self.assertEqual(response.status_code, 302)
        # count number of books
        self.assertEqual(Books.objects.count(), 2)
        # check existence of book
        self.assertTrue(Books.objects.filter(title='Test Book').exists())

    def test_add_book_unauthorized(self):
        # login as a user
        self.client.login(username='user', password='password')
        # make a POST request to the URL
        response = self.client.post(self.add_book_url, self.book_data)
        self.assertEqual(response.status_code, 302)
        # count number of books
        self.assertEqual(Books.objects.count(), 1)
        # check existence of book
        self.assertFalse(Books.objects.filter(title='Test Book').exists())

    def test_add_book_invalid_form(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # required 'title' field not filled
        self.book_data['title'] = ""
        # make a POST request to the URL
        self.client.post(self.add_author_url, self.author_data)
        response = self.client.post(self.add_book_url, self.book_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), self.add_book_url)
        self.assertFormError(
            response, 'form', 'title', 'This field is required.')
        # count number of books
        self.assertEqual(Books.objects.count(), 1)

    def test_edit_book_successfully(self):
        # login as an admin
        self.client.login(username='admin', password='password123')

        # make a post request for update
        url = reverse('books:edit_book', args=[self.book.slug])
        new_image = SimpleUploadedFile("new_book_image.jpg", b"binary_content")
        data = {
            'title': 'Updated Test Book',
            'author': 'Updated Test Author',
            'slug': 'updated-test-book',
            'description': 'This is an updated test book.',
            'image': new_image,
            'publication_year': 2023,
            'pages': 5,
            'language': 'english',
            'isbn': 12345678909,
            'dimension': '12x34',
            'price': 12.50,
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_book_unauthorized(self):
        # login as an admin
        self.client.login(username='user', password='password')
        # make a post request for update
        response = self.client.post(
            reverse('books:edit_book', args=[self.book.slug]), {
                'title': 'Update book title'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_edit_book_invalid_form(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a post request for update
        response = self.client.post(
            reverse('books:edit_book', args=[self.book.slug]), {
                'title': ''})
        self.assertEqual(response.status_code, 200)

    def test_delete_book_successfully(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a post request for update
        response = self.client.post(
            reverse('books:delete_book', args=[self.book.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('books:books'))
        self.assertFalse(Books.objects.filter(id=self.book.id).exists())

    def test_delete_book_unauthorized(self):
        # login as an admin
        self.client.login(username='user', password='password')
        # make a post request for update
        response = self.client.post(
            reverse('books:delete_author', args=[self.book.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Books.objects.filter(id=self.book.id).exists())
