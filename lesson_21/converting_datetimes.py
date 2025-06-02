from datetime import datetime, UTC


date_time_str_1 : str = "2024-11-30 17:55:59"
date_time_str_2 : str = "24-17-03T5:55:30 PM"
date_time_str_3 : str = "28-02-20 8:55:30.255 -0200"


datetime_1: datetime = datetime.strptime(date_time_str_1, "%Y-%m-%d %H:%M:%S")
datetime_2: datetime = datetime.strptime(date_time_str_2, "%y-%d-%mT%H:%M:%S %p")
datetime_3: datetime = datetime.strptime(date_time_str_3, "%y-%m-%d %H:%M:%S.%f %z")

result_datetime_str: str = datetime.strftime(datetime_1, format="%y-%m-%d %H:%M:%S.%f %z")

date_end_of_war: datetime = datetime(year=2025, month=6, day=7, hour=12, minute=35, second=16, tzinfo=UTC)
datetime_timestamp: str = datetime.strftime(date_end_of_war, "%y-%m-%d %H:%M:%S.%f %z")
print(datetime_timestamp)




