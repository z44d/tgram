import datetime
from typing import Union


class ReadableTime(datetime.datetime):
    def to_relative_time(self) -> str:
        """
        Converts the datetime object into a relative time string,
        indicating the difference between the current time and the object's time.

        Examples:
            - '5 minutes ago'
            - '2 months 3 days 4 hours 15 minutes left'
            - 'Just now'

        Returns:
            str: A human-readable string representing the time difference.
        """
        now = self.now()
        delta, prefix = (now - self, "ago") if now > self else (self - now, "left")

        seconds = delta.total_seconds()
        years = int(seconds // (365 * 24 * 60 * 60))
        seconds %= 365 * 24 * 60 * 60
        months = int(seconds // (30 * 24 * 60 * 60))
        seconds %= 30 * 24 * 60 * 60
        days = int(seconds // (24 * 60 * 60))
        seconds %= 24 * 60 * 60
        hours = int(seconds // 3600)
        seconds %= 3600
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)

        time_parts = []
        if years > 0:
            time_parts.append(f"{years} year(s)")
        if months > 0:
            time_parts.append(f"{months} month(s)")
        if days > 0:
            time_parts.append(f"{days} day(s)")
        if hours > 0:
            time_parts.append(f"{hours} hour(s)")
        if minutes > 0:
            time_parts.append(f"{minutes} minute(s)")
        if seconds > 0:
            time_parts.append(f"{seconds} second(s)")

        # Join the parts together, or return "Just now" if empty
        return " ".join(time_parts) + f" {prefix}" if time_parts else "Just now"

    def to_formatted_time(self) -> str:
        """
        Converts the datetime object into a formatted string.

        Format:
            'YYYY/MM/DD - HH:MM:SS'

        Returns:
            str: A string representation of the datetime object in the specified format.
        """
        return self.strftime("%Y/%m/%d - %H:%M:%S")


def convert_timestamp(timestamp: Union[int, float]) -> ReadableTime:
    """
    Converts a Unix timestamp into a ReadableTime object.

    Parameters:
        timestamp (int | float): A Unix timestamp.

    Returns:
        ReadableTime: A datetime object with methods to get a human-readable time difference.
    """
    return ReadableTime.fromtimestamp(timestamp)
