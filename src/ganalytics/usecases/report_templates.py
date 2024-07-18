"""Report templates for Google Analytics reports."""
from src.ganalytics.domains.constants import Metric, Dimension
from src.ganalytics.utils.errors import ReportNotFoundError
from src.ganalytics.interfaces.ilogger import ILogger
from src.ganalytics.utils.validators import BaseUseCase

from src.ganalytics.interfaces.iusecases import IReportTemplate
from src.ganalytics.interfaces.ilogger import ILogger

from injector import inject


class ReportTemplates(IReportTemplate, BaseUseCase):
    """Report templates for Google Analytics reports."""

    @inject
    def __init__(self, logger: ILogger):
        """Initialize the ReportTemplates class."""
        super(BaseUseCase, self).__init__()
        self.logger = logger

    @staticmethod
    def traffic_overview() -> dict:
        """Traffic overview report template.
        This report provides an overview of the traffic on the website. It
        includes the number of active users, sessions, etc. The report is
        useful for understanding the general traffic patterns on the website.
        """
        return {
            'metrics': [
                Metric.ACTIVE_USERS.value,
                Metric.SESSIONS.value,
                Metric.NEW_USERS.value,
                Metric.BOUNCE_RATE.value,
            ],
            'dimensions': [Dimension.DAY.value],
        }
    
    @staticmethod
    def top_pages() -> dict:
        """
        Pull the top pages report.
        This report provides data on the most viewed pages on your site.
        It includes the following:
        - Metric: The number of times each page was viewed.
        - Dimension: The url path of each page.
        """
        return {
            'metrics': [Metric.SCREEN_PAGE_VIEWS.value],
            'dimensions': [Dimension.PAGE_PATH.value],
        }
    
    @staticmethod
    def top_referrers() -> dict:
        """
        Pull the top referrers report.
        This report provides data on the top referrers to your site.
        It includes the following:
        - Metric: The number of times each page was viewed.
        - Dimension: The referrer url of each page.
        """
        return {
            'metrics': [Metric.SCREEN_PAGE_VIEWS.value],
            'dimensions': [Dimension.PAGE_REFERRER.value],
        }
    
    @staticmethod
    def user_behaviour() -> dict:
        """User behaviour report template."""
        return {
            'metrics': [
                Metric.ENGAGED_SESSIONS.value,
                Metric.SCREEN_PAGE_VIEWS_PER_USER.value,
                Metric.SCREEN_PAGE_VIEWS_PER_SESSION.value,
                Metric.USER_ENGAGEMENT_DURATION.value,
                ],
            'dimensions': [Dimension.PAGE_PATH.value],
        }
    
    def get_template(self, report_name: str):
        """This method is used to get the report template by name.

        Args:
            report_name (str): The name of the report template to get.
        Returns:
            dict: The report template
        Examples:
            >>> report_templates = ReportTemplates()
            >>> report_templates.get_template('traffic_overview')
            {'metrics': ['ga:activeUsers', 'ga:sessions'], 'dimensions': ['city']}
        
        """
        try:
            return getattr(self, report_name)()
        except AttributeError:
            self.add_error(ReportNotFoundError(f'Report template `{report_name}` not found.'))
            self.logger.error(f"Report template `{report_name}` not found.")
            return None
