"""
Metrics and Dimensions Enum for Google Analytics API

Note:
    https://ga-dev-tools.google/ga4/dimensions-metrics-explorer/
    The link above provides a list of all the metrics and dimensions available in the Google Analytics API.
"""

from enum import Enum


class Metric(Enum):
    """Metric Enum for Google Analytics API

    Reference: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics
    """
    ACTIVE_1DAY_USERS = 'active1DayUsers'
    ACTIVE_7DAY_USERS = 'active7DayUsers'
    ACTIVE_28DAY_USERS = 'active28DayUsers'
    ACTIVE_USERS = 'activeUsers'
    BOUNCE_RATE = 'bounceRate'
    ENGAGED_SESSIONS = 'engagedSessions'
    ENGAGEMENT_RATE = 'engagementRate'
    NEW_USERS = 'newUsers'
    SCREEN_PAGE_VIEWS = 'screenPageViews'
    SCREEN_PAGE_VIEWS_PER_SESSION = 'screenPageViewsPerSession'
    SCREEN_PAGE_VIEWS_PER_USER = 'screenPageViewsPerUser'
    SCROLLED_USERS = 'scrolledUsers'
    SESSIONS = 'sessions'
    SESSIONS_PER_USER = 'sessionsPerUser'
    USER_ENGAGEMENT_DURATION = 'userEngagementDuration'


class Dimension(Enum):
    """Dimension Enum for Google Analytics API
    
    Reference: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions
    """
    CITY = 'city'
    COUNTRY = 'country'
    DEVICE_CATEGORY = 'deviceCategory'
    DEVICE_MODEL = 'deviceModel'
    MOBILE_DEVICE_MODEL = 'mobileDeviceModel'
    DAY = 'day'
    DAY_OF_WEEK = 'dayOfWeek'
    FULL_PAGE_URL = 'fullPageURL'
    PAGE_LOCATION = 'pageLocation'
    PAGE_PATH = 'pagePath'
    PAGE_PATH_PLUS_QUERY = 'pagePathPlusQueryString'
    PAGE_REFERRER = 'pageReferrer'
    PAGE_TITLE = 'pageTitle'
    PLATFORM = 'platform'
    SEARCH_TERM = 'searchTerm'
    MANUAL_SOURCE = 'manualSource'
    MANUAL_SOURCE_MEDIUM = 'manualSourceMedium'
    OPERATING_SYSTEM = 'operatingSystem'
    OPERATING_SYSTEM_VERSION = 'operatingSystemVersion'
    PERCENT_SCROLLED = 'percentScrolled'

