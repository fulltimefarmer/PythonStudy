import time
import datetime

ticks = time.time()
print ("当前时间戳为:", ticks)

d1 = datetime.datetime.now()
print(d1)
ts1 = d1.timestamp()
print(ts1)
d2 = d1 + datetime.timedelta(hours=1)
print(d2)
ts2 = d2.timestamp()
print(ts2)
print(ts2 - ts1)

# interval = d2 - d1
# interval_days = interval.days
# print(interval_days)
# interval_days = interval.seconds
# print(interval_days)


