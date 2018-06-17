from .base_test import BaseTest


class TestTaskNew(BaseTest):
    """Test TaskNew"""

    def setUp(self):
        super(TestTaskNew, self).setUp()
        self.response = self.client_get(
            'tickets:task_new',
            kwargs={'ticket_pk': self.ticket.pk}
        )

    def test_get(self):
        """GET /tickets/1/task/new/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tasks/new.html"""
        self.assertTemplateUsed(self.response, 'tasks/new.html')
