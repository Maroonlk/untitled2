# 使用需要先导入
# calendar： 获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数

import calendar

cal = calendar.calendar(2017, l=0, c=5)
print(type(cal))
print(cal)

#
