```python
import datetime

# Creating datetime objects
now = datetime.datetime.now()
date = datetime.date(2022, 3, 14)
time = datetime.time(13, 30, 0)
datetime_obj = datetime.datetime(2022, 3, 14, 13, 30, 0)

# Extracting information from datetime objects
year = datetime_obj.year
month = datetime_obj.month
day = datetime_obj.day
hour = datetime_obj.hour
minute = datetime_obj.minute
second = datetime_obj.second
microsecond = datetime_obj.microsecond

# Formatting datetime objects
date_str = datetime_obj.strftime('%Y-%m-%d')
time_str = datetime_obj.strftime('%H:%M:%S')
datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

# Parsing datetime strings
datetime_obj = datetime.datetime.strptime('2022-03-14 13:30:00', '%Y-%m-%d %H:%M:%S')
date_obj = datetime.date.fromisoformat('2022-03-14')

# Arithmetic with datetime objects
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
yesterday = now - one_day
time_diff = datetime.datetime(2022, 3, 15) - datetime.datetime(2022, 3, 14)

# Timezone handling
utcnow = datetime.datetime.utcnow()
utc_timezone = datetime.timezone.utc
utcnow_with_timezone = utcnow.replace(tzinfo=utc_timezone)
local_timezone = datetime.timezone(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
localnow_with_timezone = utcnow_with_timezone.astimezone(local_timezone)

```
