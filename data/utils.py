from datetime import datetime
import pytz


def converter(*, sample_dt: str):
    date_time_object = datetime.strptime(sample_dt, "%Y/%m/%d, %H:%M:%S")

    # Not really going to deal with the whole timezone issue though :D
    # local_timezone = pytz.timezone("US/Eastern")
    # local_datetime = date_time_object.replace(tzinfo=pytz.utc)
    # local_datetime = local_datetime.astimezone(local_timezone)

    unix_time = (date_time_object - datetime(1970, 1, 1)).total_seconds()
    return date_time_object, unix_time