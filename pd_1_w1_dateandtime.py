import datetime as dt
import time as tm

# little data and time intro 

print(tm.time())
# use of fromtimestamp
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)
print('-----------------------')
# you can use year, month , day, hour, etc
print(dtnow.year)

print('-----------------------')

delta = dt.timedelta(days=100)
today = dt.date.today()
print(today)
print(today - delta)
x = today > today-delta
print( x )