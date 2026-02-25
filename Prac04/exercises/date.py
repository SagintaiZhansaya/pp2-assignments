#1
from datetime import datetime, timedelta

now = datetime.now()
day5 = timedelta(days=5)
print(now - day5)

#2
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)

#3
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print(no_microseconds)

#4
from datetime import datetime

date1 = datetime(2026, 2, 25, 12, 0, 0)
date2 = datetime(2026, 2, 26, 15, 30, 0)

difference = date2 - date1

seconds = difference.total_seconds()

print(seconds)