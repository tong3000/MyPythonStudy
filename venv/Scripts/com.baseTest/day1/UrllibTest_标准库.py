#coding:utf-8

"""
发送请求
requests其实是对urllib的进一步封装
urllib只做了解
"""
from urllib import request
res=request.urlopen("https://www.baidu.com")
print(res.status)
print(res.read())
print(res.headers)