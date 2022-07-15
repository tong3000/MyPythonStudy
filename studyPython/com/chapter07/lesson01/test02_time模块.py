#!user/bin/env python
# -*- coding: utf-8 -*-

import time
#西方时间格式标准
print(time.asctime())
# 时间戳：从纪元开始到现在的秒数
print(time.time())
# 元组格式key=value
print(time.localtime())
# 按格式输出日期
print(time.strftime("%Y年-%m月-%d日 %H:%M:%S",time.localtime()))
# 获取两天前的时间
now_timestamp = time.time()
two_pre_timestamp = now_timestamp-60*60*24*2
print(two_pre_timestamp)
time_tuple = time.localtime(two_pre_timestamp)
print(time_tuple)
print(time.strftime("%Y年-%m月-%d日 %H:%M:%S",time_tuple))
