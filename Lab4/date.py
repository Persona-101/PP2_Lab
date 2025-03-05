#exercise 1
import datetime
now = datetime.datetime.now()
tdelta1 = datetime.timedelta(days = 5)
new_date = now - tdelta1
print(new_date)

#exercise 2
tdelta2 = datetime.timedelta(days = 1)

today = datetime.datetime.now()
yesterday = today - tdelta2
tomorrow = today + tdelta2

print(today)
print(yesterday)
print(tomorrow)

#exercise 3
with_micro = datetime.datetime.now()
without_micro = with_micro.replace(microsecond = 0)
print(without_micro)

#exercise 4
date1 = datetime.datetime(2020, 1, 20, 18, 42, 10, 10000)
date2 = datetime.datetime(2023, 5, 6, 8, 20, 50, 10000)
diff = date2 - date1
print(diff.total_seconds())
