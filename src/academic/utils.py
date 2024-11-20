import datetime

from django.utils import timezone


def current_year() -> int:
    return datetime.date.today().year


def current_datetime_utc() -> datetime.datetime:
    return timezone.now
