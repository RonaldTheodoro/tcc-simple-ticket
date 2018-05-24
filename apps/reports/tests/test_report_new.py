from apps.tickets.tests.base_test import BaseTest


class TestReportNew(BaseTest):
    """Test ReportNew"""

    def setUp(self):
        super(TestReportNew, self).setUp()
        self.response = self.client_get('reports:new')

    def test_get(self):
        """GET /reports/new/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/new.html"""
        self.assertTemplateUsed(self.response, 'reports/new.html')