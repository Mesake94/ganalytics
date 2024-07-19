"""Entry point for the Google Analytics client."""
from src.ganalytics.config import configure
from src.ganalytics.interfaces.iusecases import (
    IReportUseCase,
    IReportConverter
)


injector = configure()


class ReportClient:

    def __init__(self):
        """Initialize the ReportClient class.
        This class will pull reports from the Google Analytics API
        using the ReportUseCase class.
        """
        self.reportModule = injector.get(IReportUseCase)
        self.converterModule = injector.get(IReportConverter)

    def pull_report_snapshot(self, report_name: str, date_range: dict):
        """Pull a report snapshot from the Google Analytics API.
        """
        return self.reportModule.pull_report(report_name, date_range)
    
    def pull_report_realtime(self, report_name: str):
        return self.reportModule.pull_realtime_report(report_name)
    
    def convert_report(self, report):
        """Convert a report to a table-like structure.
        """
        return self.converterModule.convert_report(report)