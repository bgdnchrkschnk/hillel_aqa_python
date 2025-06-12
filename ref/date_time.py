# Поточна дата та час
from datetime import datetime, date, time, timedelta

now = datetime.now()

# Поточна дата та час з таймзоною
from zoneinfo import ZoneInfo
now_kyiv = datetime.now(ZoneInfo("Europe/Kyiv"))

# Створити вручну
dt = datetime(2024, 5, 31, 14, 30)

print(dt.year)       # 2025
print(dt.month)      # 5
print(dt.day)        # 31
print(dt.hour)       # 14
print(dt.minute)     # 30
print(dt.weekday())  # 0 = Monday, 6 = Sunday

# Лише дата
d = date(2024, 5, 31)

# Лише час
t = time(14, 30, 0)


# У рядок
formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # '2025-05-31 12:00:00'

# З рядка
parsed = datetime.strptime("2025-05-31 12:00:00", "%Y-%m-%d %H:%M:%S")


# difference between datetime objects

dt1 = datetime(2025, 6, 1)
dt2 = datetime(2025, 5, 31)

delta = dt1 - dt2  # timedelta(days=1)
print(delta.days)  # 1

# Додати час
dt_plus = dt1 + timedelta(days=3, hours=5)