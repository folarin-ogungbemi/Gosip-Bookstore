from django.test import TestCase
from django.urls import reverse
from home.models import Contact


class TestViews(TestCase):
    """Test Views"""
    def setUp(self):
        self.contact_url = reverse('contact')

    def test_project_homePage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_project_aboutPage(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_project_teamPage(self):
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/team.html')

    def test_project_contactPage(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_contact_POST(self):
        response = self.client.post(
            self.contact_url,
            {
                'first_name': 'john', 'last_name': 'doe',
                'email': 'john.doe@emai.com', 'content': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.contact_url)
        self.assertEqual(Contact.objects.count(), 1)
