import time
import datetime

ticks = time.time()
print ("当前时间戳为:", ticks)

d1 = datetime.datetime.now()
ts1 = d1.timestamp()
ts1 = d1.timestamp()
print(ts1)
d2 = d1 + datetime.timedelta(minutes=1)
ts2 = d2.timestamp()
ts2 = d2.timestamp()
print(ts2)
d3 = d1 + datetime.timedelta(minutes=61)
ts3 = d3.timestamp()
print(ts3)

test1 = ts2 - ts1
if test1 > 3600:
    print(False)
else:
    print(True)

test2 = ts3 - ts1
if test2 > 3600:
    print(False)
else:
    print(True)

# interval = d2 - d1
# interval_days = interval.days
# print(interval_days)
# interval_days = interval.seconds
# print(interval_days)


