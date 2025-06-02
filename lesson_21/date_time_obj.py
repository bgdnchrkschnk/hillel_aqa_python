import time
from datetime import datetime, UTC, date, time

# pause code execution for some time
# time.sleep(5)
# print("Hello World!")

# create datetime object NOW
now = datetime.now(UTC)
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)
# print(now.tzinfo)


d = date(year=2020, month=12, day=31)
# print(d.day)
# print(d.year)
# print(d.month)

t = time(hour=12, minute=30, second=0)
# print(t.hour)
# print(t.minute)
# print(t.second)

dt = datetime(year=2020, month=12, day=31, hour=12, minute=30, second=0, tzinfo=UTC)
dt_2 = datetime(year=2025, month=12, day=31, tzinfo=UTC)
print(
    datetime.strftime(dt_2, format="%Y-%m-%d %H:%M:%S"),
)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.tzinfo)


print(
    datetime.now().date() # get current date now
)

print(dt > dt_2)

