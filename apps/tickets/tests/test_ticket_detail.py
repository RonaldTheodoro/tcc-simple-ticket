from django.test import TestCase
from django.urls import reverse

from ..models import User, Ticket


class TestTicketDetail(TestCase):

    def setUp(self):
        user_data = {'username': 'ronald', 'password': '123456'}
        user = User.objects.create_user(**user_data)
        ticket = Ticket.objects.create(description='test', requester=user)
        self.client.login(**user_data)
        self.response = self.client.get(
            reverse('tickets:ticket_detail', kwargs={'pk': ticket.pk}),
            follow=True
        )

    def test_get(self):
        """GET /tickets/1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use ticket_detail.html"""
        self.assertTemplateUsed(self.response, 'ticket_detail.html')