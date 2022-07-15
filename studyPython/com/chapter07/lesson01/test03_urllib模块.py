#!user/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
#调接口
response = urllib.request.urlopen("https://www.baidu.com")
#状态码
print(response.status)
#返回值
print(response.read())
#头信息
print(response.headers)