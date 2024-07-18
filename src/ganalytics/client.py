"""Entry point for the Google Analytics client."""
from src.ganalytics.config import configure
from src.ganalytics.interfaces.iusecases import (
    IReportUseCase
)


injector = configure()


class ReportClient:

    def __init__(self):
        """Initialize the ReportClient class.
        This class will pull reports from the Google Analytics API
        using the ReportUseCase class.
        """
        self.reportModule = injector.get(IReportUseCase)

    def pull_report(self, report_name: str, date_range: dict):
        """Pull a report from the Google Analytics API.
        """
        report = self.reportModule.pull_report(report_name, date_range)
        if not self.reportModule.is_valid():
            for error in self.reportModule.get_errors():
                raise error
    