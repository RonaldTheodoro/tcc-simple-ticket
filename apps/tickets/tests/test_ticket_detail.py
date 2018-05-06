from .base_test import BaseTest


class TestTicketDetail(BaseTest):
    """Test TicketDetail"""

    def setUp(self):
        super(TestTicketDetail, self).setUp()
        self.response = self.client_get(
            'tickets:detail',
            kwargs={'pk': self.ticket.pk}
        )

    def test_get(self):
        """GET /tickets/1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tickets/detail.html"""
        self.assertTemplateUsed(self.response, 'tickets/detail.html')
