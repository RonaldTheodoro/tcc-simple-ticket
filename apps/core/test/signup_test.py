from django.core.urlresolvers import reverse
from django.test import TestCase


class SignUpTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('signup'))

    def test_get(self):
        """GET /signup must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use /signup.html"""
        self.assertTemplateUsed(self.response, 'signup.html')
