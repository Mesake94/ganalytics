"""This module defines the implementation of the compile report use case.
The usecase is responsible for converting the report request data to standard
data classes that can further be post processed.
"""
from src.ganalytics.interfaces.iusecases import ICompileReport
from src.ganalytics.utils.validators import BaseUseCase
from src.ganalytics.interfaces.ilogger import ILogger

from injector import inject


class CompileReport(ICompileReport, BaseUseCase):

    @inject
    def __init__(self, logger: ILogger):
        """Initialize the CompileReport class.
        """
        super(BaseUseCase, self).__init__()
        self.logger = logger

    def compile_report(self, result):
        """Compile a report from the Google Analytics API.
        """
        