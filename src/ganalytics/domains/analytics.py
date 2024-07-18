"""Domain module for common analytics operations."""
from .base import DomainBase

from pydantic import field_validator, model_validator

from datetime import date
from typing import List


class DateRange(DomainBase):
    """Date range domain class"""
    start_date: date
    end_date: date

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        """Validate the date range"""
        if values.start_date >= values.end_date:
            raise ValueError('start_date must be less than end_date')
        return values


class MetricData(DomainBase):
    """Metric data domain class"""
    metric: str
    value: str


class DimensionData(DomainBase):
    """Dimension data domain class"""
    dimension: str
    value: str


class ReportRow(DomainBase):
    """Report row domain class"""
    metrics: List[MetricData]
    dimensions: List[DimensionData]


class GoogleAnalyticsReport(DomainBase):
    rows: List[ReportRow] = []

    def add_row(self, row: ReportRow):
        """Add a row to the report"""
        # -- add the row to the report if it doesn't already exist
        if row not in self.rows:
            self.rows.append(row)