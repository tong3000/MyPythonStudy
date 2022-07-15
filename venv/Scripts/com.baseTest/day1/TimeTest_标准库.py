
"""
time模块学习：

"""
import time

#打印西方时间格式，星期 月份 日期，时：分：秒
print(time.asctime())
#打印时间戳：10位.6位
print(time.time())
#元组形式：年份，月份，天，时分秒 星期，一年的第多少天
print(time.localtime())
#输出带格式的时间:
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#获取2天前的时间
now_timeStamp = time.time()
two_day_before = now_timeStamp-60*60*24*2
time_tuper = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuper))




#等待
time.sleep(3)
#

