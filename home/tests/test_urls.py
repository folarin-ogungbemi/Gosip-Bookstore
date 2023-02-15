from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, about, team, ContactView


class TestUrls(SimpleTestCase):
    """Test app page urls"""

    def test_home_url_resolve(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_team_url_resolve(self):
        url = reverse('team')
        self.assertEqual(resolve(url).func, team)

    def test_about_url_resolve(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_contact_view_url_resolve(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)
