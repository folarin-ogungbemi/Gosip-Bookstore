from django.test import TestCase, Client
from django.urls import reverse
from books.models import Author, Books
# authentication
from django.contrib.auth.models import User


class TestAuthorViews(TestCase):
    """Test Author views"""

    def setUp(self):
        self.client = Client()
        # create a admin user
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
        self.author_data = {
            'name': 'Test Author',
            'book_title': 'test book title',
            'about': 'testing'}
        self.books_url = reverse('books:books')
        self.add_author_url = reverse('books:add_author')
        self.author = Author.objects.create(
            name='test', book_title='book title', about='tester')

    def test_add_author_successfully(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a post request
        response = self.client.post(self.add_author_url, self.author_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('books:add_book'))
        # count number of books
        self.assertTrue(Author.objects.all().count(), 1)
        # check existence of book is true
        self.assertTrue(Author.objects.filter(name='Test Author').exists())

    def test_add_author_unauthorized(self):
        # login as a user
        self.client.login(username='user', password='password')
        # make a post request
        response = self.client.post(self.add_author_url, self.author_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        # check existence of book is false
        self.assertFalse(Author.objects.filter(name='Test Author').exists())

    def test_add_author_invalid_form(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # required 'name' field not filled
        self.author_data['name'] = ""
        # make a POST request to the URL
        response = self.client.post(self.add_author_url, self.author_data)
        self.assertEqual(
            response.request.get("PATH_INFO"), self.add_author_url)
        self.assertFormError(
            response, 'form', 'name', 'This field is required.')
        # count number of books
        self.assertEqual(Books.objects.count(), 0)

    def test_edit_author_successfully(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a post request for update
        response = self.client.post(
            reverse('books:edit_author', args=[self.author.id]), {
                'name': 'Updated Author Name',
                'book_title': 'Updated author book',
                'about': 'Update Author about'
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('books:books'))
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'Updated Author Name')
        self.assertEqual(self.author.book_title, 'Updated author book')
        self.assertEqual(self.author.about, 'Update Author about')

    def test_edit_author_unauthorized(self):
        # login as an admin
        self.client.login(username='user', password='password')
        # make a post request for update
        response = self.client.post(
            reverse('books:edit_author', args=[self.author.id]), {
                'name': 'Updated Author Name',
                'book_title': 'Updated author book',
                'about': 'Update Author about'
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_edit_author_invalid_form(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a post request for update
        response = self.client.post(
            reverse('books:edit_author', args=[self.author.id]), {
                'name': '',
                'book_title': 'Updated author book',
                'about': 'Update Author about'
            })
        self.assertEqual(response.status_code, 200)

    def test_delete_author_successfully(self):
        # login as an admin
        self.client.login(username='admin', password='password123')
        # make a post request for update
        response = self.client.post(
            reverse('books:delete_author', args=[self.author.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('books:books'))
        self.assertFalse(Author.objects.filter(id=self.author.id).exists())

    def test_delete_author_unauthorized(self):
        # login as an admin
        self.client.login(username='user', password='password')
        # make a post request for update
        response = self.client.post(
            reverse('books:delete_author', args=[self.author.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Author.objects.filter(id=self.author.id).exists())
