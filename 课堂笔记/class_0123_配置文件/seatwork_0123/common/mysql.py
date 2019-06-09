# @Time     : 2019-04-13 22:01:51
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : mysql.py
# @function : 获取数据库最大值
import pymysql
from common.config import ReadConfig


# 一次打开，多次查询，一次整体关闭
class MysqlUtil:  # 操作要定义为方法

    def __init__(self):
        # 引入配置文件-数据库
        # config = ReadConfig()
        # self.host = config.get('db', 'host')
        # self.user = config.get('db', 'user')
        # self.password = config.get('db', 'password')
        # self.port = eval(config.get('db', 'port'))

        host = "192.168.81.131"
        user = "root"
        password = "123456"
        port = 3306
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)  # 变成实例变量self.后面好引用
        self.cursor = self.mysql.cursor()  # 建立游标 查询页面。self.引用
        # print(type(host), host)
        # print(type(user), user)
        # print(type(password), password)
        # print(type(port), port)

    def fetch_one(self, sql):  # 查询数据，sql定义为方法参数
        self.cursor.execute(sql)  # 执行sql
        result = self.cursor.fetchone()  # 查询结果 fetchone一条
        return result

    def close(self):  # 一次性关闭
        self.cursor.close()  # 游标查询关闭 self.
        self.mysql.close()  # 数据库整体关闭


if __name__ == '__main__':  # 用main方法进行一次查询
    mysql = MysqlUtil()  # 实例化对象（进行了一次数据库的连接）
    # sql = "SELECT MAX(MobilePhone) FROM future.member WHERE MobilePhone LIKE '152%';"  # 传一条sql进来
    sql = "SELECT Id FROM future.loan WHERE MemberID=82 ORDER BY CreateTime DESC LIMIT 1;"
    result = mysql.fetch_one(sql)[0]  # 用变量接收
    print(result)  # 加下标，获取第一条数据。
    mysql.close()  # 用完整体关闭
    # print(mysql.__init__())
    # print(type(mysql.mysql.host), mysql.mysql.host)
    # print(type(mysql.mysql.user), mysql.mysql.user)
    # print(type(mysql.mysql.password), mysql.mysql.password)
    # print(type(mysql.mysql.port), mysql.mysql.port)


# 每次查询都打开都小关闭一次，最后整体大关闭一次
# 每次查完都关闭游标，重复
"""
class MysqlUtil:  # 操作要定义为方法

    def __init__(self):
        host = "192.168.81.131"
        user = "root"
        password = "123456"
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)  # 变成实例变量self.后面好引用

    def fetch_one(self, sql):  # 查询数据，sql定义为方法参数
        cursor = self.mysql.cursor()  # 建立游标 查询页面。self.引用
        cursor.execute(sql)  # 执行sql
        result = cursor.fetchone()  # 查询结果
        cursor.close()  # 游标查询关闭
        return result

    def close(self):
        self.mysql.close()  # 数据库整体关闭
"""
