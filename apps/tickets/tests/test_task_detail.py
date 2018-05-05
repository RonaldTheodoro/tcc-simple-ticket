from django.test import TestCase
from django.urls import reverse

from ..models import User, Ticket, Task


class TestTaskDetail(TestCase):

    def setUp(self):
        user_data = {'username': 'ronald', 'password': '123456'}
        user = User.objects.create_user(**user_data)
        ticket = Ticket.objects.create(description='test', requester=user)
        task = Task.objects.create(
            description='test',
            priority='low',
            ticket=ticket,
            creator=user,
            executor=user
        )
        self.client.login(**user_data)
        self.response = self.client.get(
            reverse(
                'tickets:task_detail',
                kwargs={'ticket_pk': ticket.pk, 'task_pk': task.pk}
            ),
            follow=True
        )

    def test_get(self):
        """GET /tickets/1/task/1/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tasks/detail.html"""
        self.assertTemplateUsed(self.response, 'tasks/detail.html')
