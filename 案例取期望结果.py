# @Time     : 2019-04-08 20:16:38
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : 案例取期望结果.py
# @function :

# 老师堂派地址：http://119.23.241.154:3306/  # 不能连接
# 同学作业地址：http://47.107.168.87:8080/  # 可以连接
# 自己本地地址：http://192.168.81.131:8888/  # 可以连接
# http://192.168.81.131:8888/futureloan/mvc/api/member/login
# ${register_mobile}

import requests

# # # 注册
# register_data = {'mobilephone': '18675512591', 'pwd': '123456'}
# register = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/register', data=register_data)
# print('响应信息 字典', register.json())

# 登陆
# register_data = {'mobilephone': '18675512599', 'pwd': 'xiuyu123'}
# login = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/login', data=register_data)
# ret_cok = login.cookies
# print('响应信息 字典', login.json())
# print(login.text)
# print('登陆返回的响应cookies', ret_cok)

# 充值
recharge_data = {'mobilephone': '18675512527', 'amount': '500000'}
recharge = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/recharge',
                         data=recharge_data, cookies=ret_cok)
print('响应信息 字典', recharge.json())
print('字典', recharge.text)

# # 提现
# withdraw_data = {"mobilephone": "18675512527", "amount": "500000"}
# withdraw = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/withdraw',
#                          data=withdraw_data, cookies=ret_cok)
# # print('响应信息 字典', recharge.json())
# print('取现post', withdraw.text)

# # 获取用户列表????????
# # list_data = {"mobilephone": "18675512527", "amount": "500000"}
# list_data = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/list', cookies=ret_cok)
# # print('响应信息 字典', recharge.json())
# print('取现post', list_data.text)

# # 投资、竞标（bidLoan）
# # bidLoan_data = {"memberId": "80", "password": "xiuyu123", "loanId": "212", "amount": "100"}
# bidLoan_data = {"memberId": "${normal_member_id}", "password": "${normal_pwd}", "loanId": "0", "amount": "100"}
# bidLoan = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/member/bidLoan',
#                          data=bidLoan_data)
# # print('响应信息 字典', recharge.json())
# print('字典', bidLoan.text)

# 新增项目（add）
# add_data = {"memberId": "82", "title": "第一次借款", "amount": "1000", "loanRate": "24", "loanTerm": "31", "loanDateType": "4", "repaymemtWay": "11", "biddingDays": "10"}
# add = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/loan/add',
#                          data=add_data)
# # print('响应信息 字典', recharge.json())
# print('字典', add.text)

# 审核
# audit_data = {"id":"212", "status": "5"}
# loan_audit = requests.post('http://192.168.81.131:8888/futureloan/mvc/api/loan/audit', data=audit_data)
# print('审核结果', loan_audit.text)



