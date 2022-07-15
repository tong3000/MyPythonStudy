#!user/bin/env python
# -*- coding: utf-8 -*-
import json

import requests

r_get = requests.get("http://www.baidu.com")
code = str(r_get.status_code)
print("状态码为"+code)
data = {
	"orderid": "TGT_S57DF452F401045C",
	"transactionid": "5AEA6654C8B",
	"operationtype": "2",
	"isdirectpay": "FALSE",
	"serialnumber": "FT5AUA664D1005B93B0A8339",
	"partnerid ": "xiaowuguicom ",
	"method ": "train_confirm ",
	"reqtime ": "20180503093126 ",
	"sign ": "916972e27 c445244f48124e36ded74c6 "
}
r_post = requests.post("http://rap2api.taobao.org/app/mock/126135/api/applysuply",data)
print(r_post.status_code)
print(r_post.text)
print(json.loads(r_post.text)["changeserial"])