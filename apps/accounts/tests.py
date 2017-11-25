from django.core.urlresolvers import reverse
from django.test import TestCase


class SignUpTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('accounts:signup'))

    def test_get(self):
        """GET /accounts/signup must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use accounts/signup.html"""
        self.assertTemplateUsed(self.response, 'accounts/signup.html')
