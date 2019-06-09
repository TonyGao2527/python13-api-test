# @Time     : 2019-04-12 00:23:55
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : study_pymysql.py
# @function : 数据库取最大值

# 先自行安装这个模块 pip install pymysql

import pymysql


# 1, 建立连接
# pymysql.connect()  # 自行进connect()里看有很多参数
host = "192.168.81.131"
user = "root"
password = "123456"
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
# 2，新建一个查询页面
cursor = mysql.cursor()  # 相当于在客户端打开一个查询页面，并返回对象

# 3，编写SQL 增删改查
sql = "SELECT MAX(MobilePhone) FROM future.member WHERE MobilePhone LIKE '152%';"  # connect里面没有加databases所以这里要加future. 这样更灵活一些
# 4，执行SQL
cursor.execute(sql)  # sql传进来
# 5，查看结果
result = cursor.fetchone()  # 返回最近的一条结果
# recult = cursor.fetchall()  # 多个元组组成的列表数据
print(result)  # 取值时元组
# 打印：('15246292536',)
print(result[0])  # 取值用索引
# 打印：15246292536
# 6，关闭查询
cursor.close()
# 7，数据库连接关闭
mysql.close()
