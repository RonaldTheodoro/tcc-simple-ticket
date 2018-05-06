from .base_test import BaseTest


class TestTicketNew(BaseTest):
    """Test TicketNew"""

    def setUp(self):
        super(TestTicketNew, self).setUp()
        self.response = self.client_get('tickets:new')

    def test_get(self):
        """GET /tickets/new/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tickets/new.html"""
        self.assertTemplateUsed(self.response, 'tickets/new.html')