import datetime

def readable_time(timestamp):
    """
    Converts a timestamp into a human-readable time-ago format.

    Parameters:
        timestamp (int): Unix timestamp or datetime object.

    Returns:
        str: Time ago in words (e.g., '5 minutes ago').
    """
    if isinstance(timestamp, int):
        timestamp = datetime.datetime.fromtimestamp(timestamp)
    delta = datetime.datetime.now() - timestamp
    
    if delta.days > 365:
        years = delta.days // 365
        return f"{years} year(s) ago"
    elif delta.days > 30:
        months = delta.days // 30
        return f"{months} month(s) ago"
    elif delta.days > 0:
        return f"{delta.days} day(s) ago"
    elif delta.seconds > 3600:
        hours = delta.seconds // 3600
        return f"{hours} hour(s) ago"
    elif delta.seconds > 60:
        minutes = delta.seconds // 60
        return f"{minutes} minute(s) ago"
    else:
        return "Just now"