from datetime import datetime, UTC, timezone, timedelta
from zoneinfo import ZoneInfo, available_timezones

# filter timezones for europe
# tz_europe = [tz for tz in available_timezones() if tz.startswith("Europe/")]
# print(tz_europe)

dt_kyiv = datetime(2025, 10, 10, 10, 10, 10, tzinfo=ZoneInfo('Europe/Kyiv'))

# astimezone - використовуємо для конвертування між таймзонами

dt_tokyo = dt_kyiv.astimezone(ZoneInfo('Asia/Tokyo'))
print(dt_kyiv)
print(dt_tokyo)

print(
    dt_kyiv.time() == dt_tokyo.time()
)

# встановити таймзону, або замінити
"""replace(tzinfo=...) не конвертує, а лише “призначає” таймзону (небезпечно для UTC → local).
Краще створити datetime одразу з таймзоною або скористатися astimezone."""
dt_tokyo = dt_kyiv.replace(tzinfo=ZoneInfo('Asia/Tokyo'))
print(dt_tokyo)

# transaction_kyiv = datetime.now(tz=ZoneInfo('Europe/Kyiv'))
# transaction_tbilisi = transaction_kyiv.astimezone(tz=ZoneInfo('Asia/Tbilisi'))

tran_dt_kyiv = datetime(2025, 6, 2, 22, 1, 10, tzinfo=ZoneInfo('Europe/Kyiv'))
tran_dt_tbilisi = tran_dt_kyiv.astimezone(tz=ZoneInfo('Asia/Tbilisi'))

print(
    tran_dt_kyiv
)
if tran_dt_tbilisi.day == tran_dt_kyiv.day:
    print("Transaction is today!")
else:
    print("Transaction is tomorrow!")




