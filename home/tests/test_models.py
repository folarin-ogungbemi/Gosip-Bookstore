from django.test import TestCase
from home.models import Contact


class TestHomeModels(TestCase):
    """Test Contact model"""
    def setUp(self):
        self.contact = Contact()
        self.contact.first_name = 'john'
        self.contact.last_name = 'doe'
        self.contact.email = 'john.doe@email.com'
        self.contact.content = "hello developer"
        self.contact.save()

    def test_contact_field_is_created(self):
        message = Contact.objects.get(id=self.contact.id)
        self.assertEqual(message, self.contact)

    def test_contact_returns_string_method(self):
        email = Contact.objects.create(email=self.contact.email)
        self.assertEqual(str(email), 'john.doe@email.com')
