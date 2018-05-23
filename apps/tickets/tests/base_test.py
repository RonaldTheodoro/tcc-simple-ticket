from django.test import TestCase
from django.urls import reverse

from ..models import Task, Ticket, User
from apps.reports.models import Report


class BaseTest(TestCase):
    """Base test configuration"""
    user_data = {'username': 'ronald', 'password': '123456'}

    def setUp(self):
        self.user = self.create_user()
        self.ticket = self.create_ticket(self.user)
        self.task = self.create_task(self.ticket, self.user)
        self.report = self.create_report(self.ticket)
        self.client_login()

    def create_user(self):
        """Create a user register"""
        return User.objects.create_user(**self.user_data)

    def create_ticket(self, user):
        """Create a ticket register"""
        return Ticket.objects.create_ticket('test', user)

    def create_task(self, ticket, user):
        """Create a task register"""
        return Task.objects.create_task('test', 'low', ticket, user, user)

    def create_report(self, ticket):
        """Create a report register"""
        report = Report.objects.create(title='test', description='test')
        report.tickets.add(self.ticket)
        report.save()
        return report 

    def client_login(self):
        """Login a user"""
        return self.client.login(**self.user_data)

    def client_get(self, url, kwargs={}):
        """Get a content"""
        return self.client.get(reverse(url, kwargs=kwargs), follow=True)
