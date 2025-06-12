from datetime import datetime, UTC
import time



row1 = '2024-11-30 17:55:59'  # UTC
row2 = '24-17-03T5:55:30.255 PM'  # UTC
row3 = '28-02-20 8:55:40.255 -0200'  # TZ = -2 години
row4 = '28-02-20'


row1_transformed = datetime.strptime(row1, '%Y-%m-%d %H:%M:%S')  # приймае строку, поверне class datetime
row2_transformed = datetime.strptime(row2, '%y-%d-%mT%H:%M:%S.%f %p')  # приймае строку, поверне class datetime
row3_transformed = datetime.strptime(row3, '%d-%m-%y %H:%M:%S.%f %z')  # приймае строку, поверне class datetime
row4_transformed = datetime.strptime(row4, '%d-%m-%y')  # приймае строку, поверне class datetime

log_entry = "2025-06-02 15:42:10"
dt = datetime.strptime(log_entry, "%Y-%m-%d %H:%M:%S")
print(dt)  # datetime object

dt = datetime(2025, 6, 2, 15, 42)
print(dt.strftime("Дата: %d/%m/%Y, час: %H:%M"))
# Дата: 02/06/2025, час: 15:42


old = "02-06-2025"
dt = datetime.strptime(old, "%d-%m-%Y")
new = dt.strftime("%Y/%m/%d")
print(new)  # 2025/06/02


date_str = "June 2, 2025"
dt = datetime.strptime(date_str, "%B %d, %Y")
print(dt.strftime("%d.%m.%Y"))  # 02.06.2025

input_date = "2025-06-01"
parsed = datetime.strptime(input_date, "%Y-%m-%d")
if parsed < datetime.now():
    print("Ця дата в минулому")

dt = datetime.now()
print(dt.strftime("%Y-%m-%dT%H:%M:%SZ"))  # 2025-06-02T14:50:00Z