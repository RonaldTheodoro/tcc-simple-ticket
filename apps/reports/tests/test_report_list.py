from apps.tickets.tests.base_test import BaseTest


class ReportListTest(BaseTest):

    def setUp(self):
        super(ReportListTest, self).setUp()
        self.response = self.client_get('reports:list')

    def test_get(self):
        """GET /reports/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/list.html"""
        self.assertTemplateUsed(self.response, 'reports/list.html')