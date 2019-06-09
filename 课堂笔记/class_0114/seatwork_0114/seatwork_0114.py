# @Time   : 2019-03-29 21:38:16
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : seatwork_0114.py

# 作业要求
"""
20190114-requests模块的练习
截至：01月16日  23:59
1，熟读前程贷需求文档，数据库结构。
（自取：https://www.ketangpai.com/Courseware/index/courseid/MDAwMDAwMDAwMLOcy5WGqads.html）
2，使用requests完成其中注册，登录，充值接口的调用 （温馨提示，充值需要传登录之后返回的cookies）
requests文档参考：（其中快速上手都照着练习一下，你会发现对requests摸得透透的！）
http://cn.python-requests.org/zh_CN/latest/
"""

# 作业2

import requests

# # 注册
# register_data = {'mobilephone': '18675512527', 'pwd': 'xiuyu123'}
# register = requests.get('http://192.168.81.131:8888/futureloan/mvc/api/member/register', params=register_data)
# print('请求url', register.request.url)
# print('响应信息', register.text)

# 老师堂派地址：http://119.23.241.154:3306/  # 不能连接
# 同学作业地址：http://47.107.168.87:8080/  # 可以连接
# 自己本地地址：http://192.168.81.131:8888/  # 可以连接
# http://47.107.168.87:8080/futureloan/mvc/api/member/login
#
# 登陆
register_data = {'mobilephone': '18675512527', 'pwd': 'xiuyu123'}
login = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/login', data=register_data)
ret_cok = login.cookies
print('响应信息 字典', login.json())
print('登陆返回的响应cookies', ret_cok)

# 充值
recharge_data = {'mobilephone': '18675512527', 'amount': '500000'}
recharge = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/recharge', data=recharge_data, cookies=ret_cok)
# print('响应信息 字典', recharge.json())
print('字典', recharge.text)


# 作业3 快速上手
# PS：看了一遍好吃力，基本上没记住啥

import requests

# 发送请求
"""
# https//www.baidu.com
r = requests.get('https://api.github.com/events')
print(r)
# 打印：<Response [200]>
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r)
# 打印：<Response [200]>
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r)
# 打印：<Response [200]>
r = requests.delete('http://httpbin.org/delete')
print(r)
# 打印：<Response [200]>
r = requests.head('http://httpbin.org/get')
print(r)
# 打印：<Response [200]>
r = requests.options('http://httpbin.org/get')
print(r)
# 打印：<Response [200]>
"""

# 传递URL参数
"""
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r)
print(r.url)
# 打印：<Response [200]>
# 打印：http://httpbin.org/get?key1=value1&key2=value2
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)  # 值为列表
print(r.url)
# 打印：http://httpbin.org/get?key1=value1&key2=value2&key2=value3
"""

# 响应内容
"""
import requests
r = requests.get('https://api.github.com/events')
# r.text
print(r.text)
# 打印：[{"id":"9345219556","type":"PushEvent"......
r.encoding
print('属性', r.encoding)
# 打印：属性 utf-8
a = r.encoding = 'ISO-8859-1'
print('修改属性', a)
# 打印：修改属性 ISO-8859-1
"""

# 二进制响应内容
"""
r = requests.get('https://api.github.com/events')
r.content
print(r.content)
# 打印：b'[{"id":"9345247689","type":"PullRequestEvent"......

# from PIL import Image
# from io import BytesIO
# i = Image.open(BytesIO(r.content))
# print(i)
# Image 和BytedIO安装不上 运行报错
"""

# JSON 响应内容
"""
import requests

r = requests.get('https://api.github.com/events')
r.json()
print('解码', r.json())
# 打印：解码 [{'id': '9345342954', 'type': 'WatchEvent'......
r.raise_for_status()
print('是否成功', r.raise_for_status())
# 打印：是否成功 None
"""

# 原始响应内容
"""
r = requests.get('https://api.github.com/events', stream=True)
print('原始数据', r.raw)
print('啥东西', r.raw.read(10))
# 打印：原始数据 <urllib3.response.HTTPResponse object at 0x0000014BF6221A20>
# 打印：啥东西 b'\xed}Y\x8f\x1bW\x96\xe6_\t'

# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size):
#         fd.write(chunk)
# 运行报错

# Response.iter_content
# 运行报错
"""

# 定制请求头
"""
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
print(r.request.headers)
# 打印：{'user-agent': 'my-app/0.0.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
"""

# 更加复杂的 POST 请求
"""
# 递一个字典给 data 参数 — — 非常像一个 HTML 表单
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
# {
#   ...
#   "form": {
#     "key1": "value1", 
#     "key2": "value2"
#   }
#   ...
"""
"""
# 传入一个元组列表  
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
# {
#   ...
#   "form": {
#     "key1": [
#       "value1",
#       "value2"
#     ]
#     ...
"""

"""
import json

# string 而不是一个 dict
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)
# 打印：{"message":"Not Found","documentation_url":"https://developer.github.com/v3"}
"""

"""
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r.text)
# 打印：{"message":"Not Found","documentation_url":"https://developer.github.com/v3"}
"""

# POST一个多部分编码(Multipart-Encoded)的文件
"""
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
print(r.text)
# {
#   ...
#   "files": {
#     "file": "data:application/...ODAwMM3yxbfUqqOssN3Iysepz8LCrL+oy7kNCg=="
#   },
#   ...
# }
"""
"""
# 显式地设置文件名，文件类型和请求头
url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
print(r.text)
# {
#   ...
#   "files": {
#     "file": "data:application/vnd.ms-excel;base64,ODAwMM3yxbfUqqOssN3Iysepz8LCrL+oy7kNCg=="
#   }, 
#   ...
# }
"""

"""
# 如果你想，你也可以发送作为文件来接收的字符串：
url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
print(r.text)
# {
#   ...
#   "files": {
#     "file": "some,data,to,send\\nanother,row,to,send\\n"
#   },
#   ...
# }
"""

# 响应状态码
"""
r = requests.get('http://httpbin.org/get')
print(r.status_code)
# 打印：200
r.status_code == requests.codes.ok
print(r.status_code)
# 打印：200

# 抛出异常  Response.raise_for_status()
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# 打印：404
# print(bad_r.raise_for_status())  # 抛出异常
# # Traceback (most recent call last):
# #   File "requests/models.py", line 832, in raise_for_status
# #     raise http_error
# # requests.exceptions.HTTPError: 404 Client Error
print(r.raise_for_status())
# 打印：None
"""

# 响应头
"""
r = requests.get('http://httpbin.org/get')
print(r.headers)
# 打印：{...'Content-Encoding': 'gzip', 'Content-Type': 'application/json'...}
print(r.headers['Content-Type'])
# 打印：application/json
print(r.headers.get('content-type'))
# 打印：application/json
"""

# Cookie
"""
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
rb = r.cookies['example_cookie_name']
# 报错：KeyError: "name='example_cookie_name', domain=None, path=None"
"""

"""
# 发送你的cookies到服务器
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
# 打印：'{"cookies": {"cookies_are": "working"}}'
"""

"""
# 把 Cookie Jar 传到 Requests 中：
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)
# 打印：{"cookies": {"tasty_cookie": "yum"}}
"""

# 重定向与请求历史
"""
# Github 将所有的 HTTP 请求重定向到 HTTPS：
[<Response [301]>]
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)
# 打印：https://github.com/
# 打印：200
# 打印：[<Response [301]>]
"""

"""
# GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，通过 allow_redirects 参数禁用重定向处理：
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)
# 打印：301
# 打印：[]
"""

"""
# 如果你使用了 HEAD，你也可以启用重定向：
r = requests.head('http://github.com', allow_redirects=True)
print(r.url)
print(r.history)
# 打印：https://github.com/
# 打印：[<Response [301]>]
"""

# 超时
"""
r = requests.get('http://github.com', timeout=0.001)
"""

# 错误与异常
"""
"""

