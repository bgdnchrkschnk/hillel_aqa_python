from datetime import timedelta, datetime, UTC, timezone
from zoneinfo import ZoneInfo

now_utc = datetime.now(UTC)

now_utc_in_two_days = now_utc + timedelta(days=2, hours=2)

print(now_utc)
print(now_utc_in_two_days)

# -----------------

start = datetime(2025, 6, 1)
end = datetime(2025, 6, 5)



def get_timedelta(dt_1: datetime, dt_2: datetime) -> timedelta:
    return abs(dt_2 - dt_1)

# delta: timedelta = get_timedelta(start, end)
# print(
#     delta
# )


dt_tokyo = datetime.now(tz=ZoneInfo('Asia/Tokyo'))
dt_utc = datetime.now(tz=ZoneInfo('UTC'))
dt_utc_converted_to_tokyo = dt_utc.replace(tzinfo=ZoneInfo('Asia/Tokyo'))

print(
    dt_tokyo, dt_utc_converted_to_tokyo
)

print(get_timedelta(dt_tokyo, dt_utc_converted_to_tokyo))