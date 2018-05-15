from .base_test import BaseTest


class ReportDetailTest(BaseTest):

    def setUp(self):
        super(ReportDetailTest, self).setUp()
        self.response = self.client_get(
            'tickets:report_detail',
            kwargs={'pk': self.report.pk}
        )

    def test_get(self):
        """GET /tickets/reports/1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/detail.html"""
        self.assertTemplateUsed(self.response, 'reports/detail.html')
