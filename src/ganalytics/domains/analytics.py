"""Domain module for common analytics operations."""
from .base import DomainBase

from pydantic import field_validator, model_validator

from datetime import date


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
