from abc import ABCMeta, abstractmethod


class IReportUseCase(metaclass=ABCMeta):
    """Interface for the report use case. This interface defines the methods
    that the report use case should implement.
    """

    @abstractmethod
    def pull_report(self, report_name: str, date_range: dict):
        """Pull a report from the Google Analytics API.
        """
        raise NotImplementedError


class IReportTemplate(metaclass=ABCMeta):
    """Interface for the report template. This interface defines the methods
    that the report template should implement.
    """

    @abstractmethod
    def get_template(self, report_name: str):
        """Get the report template by name.
        """
        raise NotImplementedError
    

class ICompileReport(metaclass=ABCMeta):
    """Interface for the compile report use case. This interface defines the methods
    that the compile report use case should implement.
    """

    @abstractmethod
    def compile_report(self, *args, **kwargs):
        """Compile a report from the Google Analytics API.
        """
        raise NotImplementedError
    

