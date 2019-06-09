# @Time     : 2019-04-25 12:40:40
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : context.py
# @function : 反射替换_写一个正则的函数+for循环

import re  # 引入正则
# s 是目标字符串
# d 是替换的内容
# 找到目标字符串里面的标识符KEY，去d里面拿到替换的值
# 替换到s 里面去，然后再返回
from common.config import ReadConfig  # 引入读配置文件
config = ReadConfig()  # 创建对象
class Context:  # 上下文，数据的准备和记录
    admin_user = config.get('data', 'admin_user')  # 管理员电话
    admin_pwd = config.get('data', 'admin_pwd')  # 管理员密码
    loan_member_id = config.get('data', 'loan_member_id')  # 管理员id
    normal_user = config.get('data', 'normal_user')  # 投资人电话
    normal_pwd = config.get('data', 'normal_pwd')  # 投资人密码
    normal_member_id = config.get('data', 'normal_member_id')  # 投资人id


def replace(s, d):
    p = "\$\{(.*?)}"  # 正则查找一次
    while re.search(p, s):  # 解析, 再s里面找p, 加循环
        m = re.search(p, s)  # 创建match对象
        key = m.group(1)  # 取里面的key admin_user
        value = d[key]  # 取字典的key的值
        s = re.sub(p, value, s, count=1)# 替换，再从新赋值为s
    return s  # 返回被替换的字符串


def replace_new(s):
    p = "\$\{(.*?)}"  # 正则查找一次
    while re.search(p, s):  # 解析, 再s里面找p, 加循环
        m = re.search(p, s)  # 创建match对象
        key = m.group(1)  # 取里面的key admin_user
        # 最好加判断是否有属性，有执行，没有就return None
        if hasattr(Context, key):  # 判断当前这个类有没有这个属性，有就返回True，没有就返回False 不会报错。
            value = getattr(Context, key)  # 利用反射动态的获取属性
            s = re.sub(p, value, s, count=1)  # 替换，再从新赋值为s
        else:
            return None  # 或者抛除一个异常，告知没有这个属性
    return s  # 返回被替换的字符串


if __name__ == '__main__':

    s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
    # data = {"admin_user": "18675512527", "admin_pwd": "xiuyu123"}
    #
    # s = replace(s, data)
    # print(s)
    # # 打印：{"mobilephone":"18675512527","pwd":"xiuyu123"}

    s = replace_new(s)
    print(s)
    # 打印：{"mobilephone":"18675512527","pwd":"xiuyu123"}



