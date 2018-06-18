import datetime
import time

# datetime常见属性
# datetime.date ：一个理想和的日期，提供year， month， day 属性


print(datetime.date(2018, 6, 18))

# datetime.time: 提供一个理想和的时间，

# datetime.datetime: 提供日期跟时间的组合

# datetime.timedelta: 提供一个四件差，时间长度

from datetime import datetime

# 常用类方法：
# today：
# now：
# utcnow：
# fromtimestamp： 从时间戳返回本地时间
dt = datetime(2018, 3, 26)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta
# 表示一个时间间隔

from datetime import datetime, timedelta

t1 = datetime.now()
print(t1)

print(t1.strftime("%Y - %m - %d  %H:%S"))
# 以td表示以小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y - %m - %d  %H:%S"))

