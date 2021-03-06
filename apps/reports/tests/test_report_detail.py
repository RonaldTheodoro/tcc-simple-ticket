from apps.tickets.tests.base_test import BaseTest


class ReportDetailTest(BaseTest):

    def setUp(self):
        super(ReportDetailTest, self).setUp()
        self.response = self.client_get(
            'reports:detail',
            kwargs={'pk': self.report.pk}
        )

    def test_get(self):
        """GET /reports/1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/detail.html"""
        self.assertTemplateUsed(self.response, 'reports/detail.html')
