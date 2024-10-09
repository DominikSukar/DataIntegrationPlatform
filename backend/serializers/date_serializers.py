from datetime import datetime


def datetime_serializer(dt: datetime) -> str:
    "This serializer is used to convert any datetime object to a following standard"
    return dt.strftime("%Y-%m-%d %H:%M:%S")
