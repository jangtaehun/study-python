import datetime

#현재 날짜
now = datetime.date.today()
now_time = datetime.datetime.today()
print(now)
print(now_time)
print(now.year)
print(now.month)
print(now.day)
print(now_time.hour)
print(now_time.minute)
print(now_time.second)

#지정된 날짜
date = datetime.datetime(2024, 1, 1, 12, 0, 0)
print(date)