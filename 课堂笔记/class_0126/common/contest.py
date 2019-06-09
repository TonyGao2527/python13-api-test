# @Time     : 2019-04-25 12:40:40
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : context.py
# @function : 写一个正则的函数+for循环

import re  # 引入正则
# s 是目标字符串
# d 是替换的内容
# 找到目标字符串里面的标识符KEY，去d里面拿到替换的值
# 替换到s 里面去，然后再返回


def replace(s, d):
    p = "\$\{(.*?)}"  # 正则查找一次
    while re.search(p, s):  # 解析, 再s里面找p, 加循环
        m = re.search(p, s)  # 创建match对象
        key = m.group(1)  # 取里面的key admin_user
        value = d[key]  # 取字典的key的值
        s = re.sub(p, value, s, count=1)# 替换，再从新赋值为s
    return s  # 返回被替换的字符串


data = {"admin_user": "18675512527", "admin_pwd": "xiuyu123"}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'

s = replace(s, data)
print(s)
# 打印：{"mobilephone":"18675512527","pwd":"xiuyu123"}





