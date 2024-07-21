"""Injector configuration to bind the test classes to their implementations."""
from injector import Injector, singleton

from ganalytics.interfaces.ianalytics import IAnalyticsAPI
from ganalytics.interfaces.iusecases import IReportUseCase, IReportTemplate, IReportConverter
from ganalytics.interfaces.ilogger import ILogger

from ganalytics.usecases.pull_reports import PullReport
from ganalytics.usecases.report_templates import ReportTemplates
from ganalytics.usecases.converter import ReportConverter
from ganalytics.infrastructure.google_analytics_api import GoogleAnalyticsAPI
from ganalytics.infrastructure.logger import Logger

from tests.mocks import *


def configure():
    """Configure the injector"""
    injector = Injector()
    injector.binder.bind(IAnalyticsAPI, to=GoogleAnalyticsAPI, scope=singleton)
    injector.binder.bind(IReportUseCase, to=PullReport, scope=singleton)
    injector.binder.bind(ILogger, to=Logger, scope=singleton)
    injector.binder.bind(IReportTemplate, to=ReportTemplates, scope=singleton)
    injector.binder.bind(IReportConverter, to=ReportConverter, scope=singleton)
    return injector