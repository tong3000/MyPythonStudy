"""
python第三方库
测试框架：pytest
get/post
"""
import requests

res = requests.get("http://www.baidu.com")
print(res.status_code)
print(res.encoding)
print(res.text)

