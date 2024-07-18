"""Injector configuration to bind the test classes to their implementations."""
from injector import Injector, singleton

from src.ganalytics.interfaces.ianalytics import IAnalyticsAPI
from src.ganalytics.interfaces.iusecases import IReportUseCase, IReportTemplate
from src.ganalytics.interfaces.ilogger import ILogger

from src.ganalytics.usecases.pull_reports import PullReport
from src.ganalytics.usecases.report_templates import ReportTemplates
from src.ganalytics.infrastructure.google_analytics_api import GoogleAnalyticsAPI
from src.ganalytics.infrastructure.logger import Logger

from tests.mocks import *


def configure():
    """Configure the injector"""
    injector = Injector()
    injector.binder.bind(IAnalyticsAPI, to=GoogleAnalyticsAPI, scope=singleton)
    injector.binder.bind(IReportUseCase, to=PullReport, scope=singleton)
    injector.binder.bind(ILogger, to=Logger, scope=singleton)
    injector.binder.bind(IReportTemplate, to=ReportTemplates, scope=singleton)
    return injector