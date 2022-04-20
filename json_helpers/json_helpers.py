"""Main module."""
import json
from datetime import datetime


def datetime_str(value: datetime) -> str:
    return value.strftime("%Y-%m-%dT%H:%M:%S.%f")


def datetime_from_standard_str(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")


class JSONEncoderWithDateHandling(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return datetime_str(obj)

        return obj
