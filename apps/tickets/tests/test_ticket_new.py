from django.test import TestCase
from django.urls import reverse

from ..models import User


class TestTicketNew(TestCase):

    def setUp(self):
        user_data = {'username': 'ronald', 'password': '123456'}
        user = User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.response = self.client.get(
            reverse('tickets:new_ticket'),
            follow=True
        )

    def test_get(self):
        """GET /tickets/new_ticket/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use open_ticket.html"""
        self.assertTemplateUsed(self.response, 'open_ticket.html')