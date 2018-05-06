from django.test import TestCase
from django.urls import reverse

from ..models import User


class TestTicketList(TestCase):
    """Test TicketList"""

    def setUp(self):
        user_data = {'username': 'ronald', 'password': '123456'}
        User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.response = self.client.get(reverse('tickets:list'), follow=True)

    def test_get(self):
        """GET /tickets/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tickets/list.html"""
        self.assertTemplateUsed(self.response, 'tickets/list.html')

