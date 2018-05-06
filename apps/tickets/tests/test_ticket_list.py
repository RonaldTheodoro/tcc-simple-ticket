from .base_test import BaseTest


class TestTicketList(BaseTest):
    """Test TicketList"""

    def setUp(self):
        super(TestTicketList, self).setUp()
        self.response = self.client_get('tickets:list')

    def test_get(self):
        """GET /tickets/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tickets/list.html"""
        self.assertTemplateUsed(self.response, 'tickets/list.html')

