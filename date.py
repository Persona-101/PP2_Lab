#exercise 1
from datetime import datetime, timedelta
today = datetime.today()
new_date = today - timedelta(days=5)
print(new_date)

#exercise 2
from datetime import datetime, timedelta
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", today.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))

#exercise 3
from datetime import datetime
now = datetime.now()
now_without_microseconds = now.replace(microsecond=0)
print("Original datetime:", now)
print("Datetime without microseconds:", now_without_microseconds)

#exercise 4
from datetime import datetime
date1 = datetime(2024, 2, 10, 12, 30, 15) 
date2 = datetime(2024, 2, 12, 14, 45, 30)  
difference = abs((date2 - date1).total_seconds())
print("Difference in seconds:", difference)
