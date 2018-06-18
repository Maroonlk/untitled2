# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用 理论上都应该先带入，string是特例
- calendar， time， datetime， 的区别参开中文意思
# calendar
- 跟日历相关的模块
    - 案例  calendar模块.py
    
    ### isleap： 判断某一年是否闰年
    ### leapdays: 获取指定年份之间 闰年的个数
    ### month： 获取某个月的日历字符串
        - 格式 calender.leapdays(年, 月)
        - 返回值： 月日历的字符串
        
    ### monthrange（） 获取一个月的一号是周几和这个月的天数
        - 格式 calendar.monthrange(年，月)
        - 返回值： 元祖（周几开始，总天数）
        - 注意： 周默认 0-6 表示周一到周日
        
    ### monthcalendar（） 返回一个月每天的矩阵列表
        - 格式 calendar.monthcalendar(年，月）
        - 返回值： 二级列表
        - 注意： 矩阵中没有天数的话 用 0表示
        
    ### prcal：（print calendar的缩写） 直接打印日历
    
    ### prmonth（）  直接打印某个月的日历
        - 格式 ： calendar.prmonth（年，月）
        - 返回值： 无
    
    ### weekday（） 获取周几
        - 格式： （年，月，日）



# time模块
### 时间戳
- 一个时间表示，根据不同语言，可以是整数也可以是浮点数
- 是从1970年1月1日0时0分0秒到现在经历的秒数
- 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
- 32位操作系统能够支持到2038年

### UTC时间
- UTC又称为世界协调时间，以英国的格林尼治天文所在的地区的时间作为参开时间
，也叫做世界标准时间。
- 中国时间是 UTC+8 东八区

### 夏令时
- 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起节省蜡烛！每天变成25个小时
，本质没变还是24个小时。

### 时间元祖
- 一个包含时间内容的普通元祖


        索引      内容      属性      值
        0         年      tm_year   2015
        1         月      tm_mon    1~12
        2         日      tm_mday   1~31
        3         时      tm_hour   0~23
        4         分      tm_min    0~59
        5         秒      tm_sec    0~61   60表示闰秒  61保留值
        6       周几     tm_wday    0~6
        7       第几天     tm_yday   1~366
        8       夏令时     tm_isdst  0,1，-1
- 需要单独导入

- 得到时间戳
    - time.time()