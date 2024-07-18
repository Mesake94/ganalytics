from src.ganalytics.interfaces.ianalytics import (
    IAnalyticsAPI
)
from src.ganalytics.interfaces.ilogger import ILogger
from src.ganalytics.domains.constants import (
    Metric as MetricEnum,
    Dimension as DimensionEnum,
)
from src.ganalytics.utils.validators import BaseAPI
from src.ganalytics.utils.errors import (
    EnvironmentVariableError,
    GoogleAnalyticsAPIError,
)

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Metric,
    Dimension,
    RunReportRequest,
)

import os

from injector import inject


class GoogleAnalyticsAPI(IAnalyticsAPI, BaseAPI):
    """Google Analytics API class"""

    @inject
    def __init__(self, logger: ILogger):
        """Initialize the Google Analytics API"""
        self.logger = logger
        super(BaseAPI, self).__init__()
        self.__post_init__()

    def check_env_vars(self, env_vars: list):
        """Check if required environment variables are set
        """
        for env_var in env_vars:
            if not os.getenv(env_var):
                self.add_error(
                    EnvironmentVariableError(
                        f"Environment variable {env_var} is not set."
                    )
                )
                self.logger.error(f"Environment variable {env_var} is not set.")

    def __post_init__(self):
        """Post initialization method"""
        # -- check if required environment variables are set
        self.check_env_vars([
            'GA_PROPERTY_ID',
            'GOOGLE_APPLICATION_CREDENTIALS',
        ])
        try:
            self.client = BetaAnalyticsDataClient()
        except Exception as e:
            self.add_error(e)
            self.logger.error(e)

    def get_report(self, start_date: str, end_date: str, metrics: list, dimensions: list) -> dict:
        """Get report from the Google Analytics API
        """
        response = None
        try:
            # -- create a request
            request = RunReportRequest(
                property=f"properties/{os.getenv('GA_PROPERTY_ID')}",
                date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
                metrics=[Metric(name=metric) for metric in metrics],
                dimensions=[Dimension(name=dimension) for dimension in dimensions],
            )
            # -- get the report
            response = self.client.run_report(request)
        except Exception as e:
            self.add_error(GoogleAnalyticsAPIError(f"Error getting report: {e}"))
            self.logger.error(f"Error getting report: {e}")
        return response
        