# @Time   : 2019-03-31 10:53:18
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : class_0116.py

import requests
# 老师作业地址：http://47.107.168.87:8080/  # 可以连接
# 自己本地地址：http://192.168.81.131:8888/  # 可以连接
session = requests.session()  # 实例一个session,同一个session之间cookies可以共享，但是不同session之间不可以，如session2
data = {'mobilephone': '1867551252', 'pwd': 'xiuyu123'}
# 登陆
resp = session.request('post', url='http://192.168.81.131:8888/futureloan/mvc/api/member/login', data=data)
print(resp.text)
# 充值
data = {'mobilephone': '18675512527', 'amount': '37000'}
resp = session.request('post', url='http://192.168.81.131:8888/futureloan/mvc/api/member/recharge', data=data)
print(resp.text)

# 注意：cookie的有效期时30分钟之内
# 注意：相同的对象名字创建两次cookie也不同