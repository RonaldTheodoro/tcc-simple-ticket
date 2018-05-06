from .base_test import BaseTest


class TestTicketEdit(BaseTest):
    """Test TicketEdit"""

    def setUp(self):
        super(TestTicketEdit, self).setUp()
        self.response = self.client_get(
            'tickets:edit',
            kwargs={'pk': self.ticket.pk}
        )

    def test_get(self):
        """GET /tickets/1/edit must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tickets/edit.html"""
        self.assertTemplateUsed(self.response, 'tickets/edit.html')
