from django.test import TestCase
from django.urls import reverse

from apps.tickets.models import User


class HomeTest(TestCase):
    """Home Test"""

    def setUp(self):
        user_data = {'username': 'ronald', 'password': '123456'}
        User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.response = self.client.get(reverse('core:index'), follow=True)

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
