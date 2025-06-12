from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2025, 5, 31, 12, 0, tzinfo=ZoneInfo("Europe/Kyiv"))
print(dt)


# Converting between timezones

from datetime import datetime
from zoneinfo import ZoneInfo

dt_kyiv = datetime(2025, 5, 31, 12, 0, tzinfo=ZoneInfo("Europe/Kyiv"))
dt_ny = dt_kyiv.astimezone(ZoneInfo("America/New_York"))

print(f"Kyiv: {dt_kyiv}")
print(f"New York: {dt_ny}")

# -------

now_utc = datetime.now(tz=ZoneInfo("UTC"))
now_kyiv = now_utc.astimezone(ZoneInfo("Europe/Kyiv"))
print(now_kyiv)

# ------------------------------------ listing all supported timezones

from zoneinfo import available_timezones

# Це повертає множину з назвами усіх доступних таймзон
all_timezones = available_timezones()

# Наприклад, вивести перші 10
for tz in sorted(list(all_timezones)):
    print(tz)

# ---------
"""get region timezones"""

tz_europe = [tz for tz in available_timezones() if tz.startswith("Europe/")]


# Set timezone for datetime obj (NOT converting!)
"""replace(tzinfo=...) не конвертує, а лише “призначає” таймзону (небезпечно для UTC → local).
Краще створити datetime одразу з таймзоною або скористатися astimezone."""

from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime(2024, 5, 30, 12, 0, 0)
kyiv_time = dt.replace(tzinfo=ZoneInfo("Europe/Kyiv"))
print(kyiv_time)

