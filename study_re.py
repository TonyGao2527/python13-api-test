# @Time     : 2019-04-20 16:14:18
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : study_re.py
# @function : 正则替换的基本用法search()、group()、sub()

import json
import re  # 引入正则表达式，相当于在线编辑器

admin_user = '18675512527'
admin_pwd = 'xiuyu123'

data = {"admin_user": "18675512527", "admin_pwd": "123456"}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
p = "\$\{admin_user}"  # 原本字符写法\$\符号要加斜杠转义
p1 = "\$\{(.*?)}"  # 元字符和限定符，()代表组括号前后内容分别代表开始和结束内容 .任意字符 *多个 ?最多找到一个
p2 = "\$\{(.*)}"
# 在s里面找p，p是表达式
m = re.search(p, s)  # def search(pattern, string, flags=0):  def search(正则, 文件名, 匹配大小写):
print("p匹配对象", m)  # search()只找一个
m1 = re.search(p1, s)  # 任意位置开始找，找到一个就返回match
print("任意位置开始找，找到一个就返回match", m1)  # re.search()有就返回match对象，没有就返回None
m2 = re.search(p2, s)
print("p2匹配对象", m2)
# 打印：p匹配对象 <_sre.SRE_Match object; span=(16, 29), match='${admin_user}'>
# 打印：任意位置开始找，找到一个就返回match <_sre.SRE_Match object; span=(16, 29), match='${admin_user}'>
# 打印：p2匹配对象 <_sre.SRE_Match object; span=(16, 52), match='${admin_user}","pwd":"${admin_pwd}"}'>
# span指匹配的位置 16是指开始，29是指结尾。match是指匹配的内容。
# 用了正则结果相同
# 没加问好？会多搜索出一个 会一直往后面找，找到最后一个右边界)"为止

# 组
g = m1.group()  # 返回的是整个匹配的字符串
print(g)
# 打印：${admin_user}
g1 = m1.group(1)  # 取第一个组的匹配字符串，如果是第二个组就写2
print(g1)
# 打印：admin_user
value = data[g1]
# s = s.replace('${admin_user}', value)  # 这种方法不ok。查找替换
# s = re.sub(p1, value, s)  # 查找且替换 re.sub(正则查找, 新值, string, 替换次数=0, flags=0)
# print("使用正则表达式查找并且替换", s)  # 全部替换了，不ok
# # 打印：使用正则表达式查找并且替换 {"mobilephone":"18675512527","pwd":"18675512527"}
s = re.sub(p1, value, s, count=1)  # 默认查找全部
print("使用正则表达式查找并且替换", s)  # 加 count=1 指替换一次
# 打印：使用正则表达式查找并且替换 {"mobilephone":"18675512527","pwd":"${admin_pwd}"}

l = re.findall(p1, s)  # 查找全部（这里两个就是全部），返回一个列表。没有就返回空列表。re.sub()使用的就是这个findall
print("查找全部，返回一个列表", l)  # 先注释掉上面的sub，否则列表只有一个元素
# 打印：查找全部，返回一个列表 ['admin_user', 'admin_pwd']

# 指找到一个替换还不够，需要两个替换不同的


# # 将字符串转成字典，然后根据KEY去取值，渠道值判断是否需要替换
# dict1 = json.loads(s)
# if dict1['mobilephone'] == '${admin_user}':
#     dict1['mobilephone'] = admin_user
#
# print(dict1)

# 字符串的查找find()、替换replace()
if s.find('${admin_user}') > -1:  # 如果=-1是没有，>-1是有
    s = s.replace('${admin_user}', admin_user)  # 重新去复制s= 才能替换打印成功
if s.find('${admin_pwd}') > -1:
    s = s.replace('${admin_pwd}', admin_pwd)
print(s)
