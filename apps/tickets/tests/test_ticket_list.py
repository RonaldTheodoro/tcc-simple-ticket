from django.test import TestCase
from django.urls import reverse

from apps.tickets.models import User


class TestTicketList(TestCase):

    def setUp(self):
        user_data = {'username': 'ronald', 'password': '123456'}
        User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.response = self.client.get(reverse('tickets:list'), follow=True)

    def test_get(self):
        """GET /tickets/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use list.html"""
        self.assertTemplateUsed(self.response, 'list.html')

