#!/usr/bin/python3

# from datetime import timedelta
# from datetime import date
# from datetime import datetime

# #print(date(2018, 11, 1).weekday())
# print(date(2018, 11, 1).isocalendar())

from datetime import datetime, date, time
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)

dt = datetime.today()
dt

ic = dt.isocalendar()
for it in ic:   
   print(it)

# 2006    # ISO year
# 47      # ISO week
# 2       # ISO weekday
# Formatting datetime
dt.strftime("%A, %d. %B %Y %I:%M%p")
'Tuesday, 21. November 2006 04:30PM'
'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")
'The day is 21, the month is November, the time is 04:30PM.'