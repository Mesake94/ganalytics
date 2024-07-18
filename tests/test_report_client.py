import unittest
import os

from src.ganalytics.client import ReportClient


class ReportClientTestCase(unittest.TestCase):
    """Test case for the report client"""

    def setUp(self):
        # setup environment variables
        os.environ['GA_PROPERTY_ID'] = '450165182'
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tests/secrets/google-analytics-key.json'
        # get the report usecase
        self.client = ReportClient()

    def test_report_client(self):
        """Test the report client."""
        self.assertIsNotNone(self.client)

        self.client.pull_report(
            report_name='s',
            date_range={
                'start_date': '2024-01-01',
                'end_date': '2023-08-31'
            }
        )


if __name__ == "__main__":
    unittest.main()