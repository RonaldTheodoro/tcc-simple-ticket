from .base_test import BaseTest


class ReportListTest(BaseTest):

    def setUp(self):
        super(ReportListTest, self).setUp()
        self.response = self.client_get('tickets:report_list')

    def test_get(self):
        """GET /tickets/reports/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/list.html"""
        self.assertTemplateUsed(self.response, 'reports/list.html')