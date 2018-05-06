from .base_test import BaseTest

class TestTaskDetail(BaseTest):
    """Test TaskDetail"""

    def setUp(self):
        super(TestTaskDetail, self).setUp()
        self.response = self.client_get(
            'tickets:task_detail',
            kwargs={'ticket_pk': self.ticket.pk, 'task_pk': self.task.pk}
        )

    def test_get(self):
        """GET /tickets/1/task/1/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tasks/detail.html"""
        self.assertTemplateUsed(self.response, 'tasks/detail.html')
