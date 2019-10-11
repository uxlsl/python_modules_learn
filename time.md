# time


## 思考
为什么使用UNIX时间戳？
垮平台性

转换

+ 将时间滴打印time.time -> time.ctime
+ 将时间滴转换为struct time  time.time -> time.gmtime
+ 将struct time 转换为 time time.gmtime -> time.mktime
