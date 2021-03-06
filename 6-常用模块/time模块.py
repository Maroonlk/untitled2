import time

# 时间模块的属性
# timezone：当前时区和utc时间相差的秒数，在没有夏令时的情况下的间隔

print(time.timezone)

# altzone： 获取当前时区与utc时间相差的秒数，在有夏令时的情况下

print(time.altzone)

# daylight： 测当前是否是夏令时时间状态， 0表示是

print(time.daylight)

# time.time()： 得到时间戳

print(time.time())

# time.localtime()： 得到本地时间的一个结构
# 可以通过点号操作符得到想要的属性

print(time.localtime().tm_hour)

# asctime()  返回元祖的正常字符串化后的时间格式

t = time.localtime()

tt = time.asctime(time.localtime())
print(tt)

# ctime: 获取字符串化的当前时间

t = time.ctime()
print(t)

# mktime： 使用时间元祖获取对应的时间戳

lt = time.localtime()
ts = time.mktime(lt)
print(ts)



# clock： 获取CPU时间， 3.0 = 3.3 版本之间可以直接使用
# 3.6 调用有问题


# sleep： 使程序进入睡眠，n秒后继续
for i in range(1,10):
    pass
    # print(i)
    # time.sleep(1)

# srtftime: 将时间元祖转化为自定义的字符串格式
# 最常用的： 把时间表示成   2018 3.26 21:05
t = time.localtime()
# ft = time.strftime("%Y年%m月%d日 %H:%M", t)
#
# print(ft)

print("{0}年{1}月{2}日 {3}:{4}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))


# datetime模块
# datetime提供日期和时间的运算和表示
