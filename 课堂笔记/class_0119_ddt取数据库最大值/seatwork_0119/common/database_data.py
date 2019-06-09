# @Time   : 2019-04-09 21:04:31
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : database_data.py

# 自己百度查找 读取数据库的脚本----但是失败了
import mysql.connector


class MysqlData:

    def connect_mysql(self):
        # config = {'host': '192.168.81.131', 'user': 'root', 'password': '123456', 'port': '3306', 'database': 'future', 'charset':'utf8'}
        # host="192.168.81.131", user="root", password="123456", port="3306", database="future", charset="utf8"  **config
        conn = mysql.connector.connect(host="192.168.81.131", user="root", password="123456", port="8888", database="future", charset="utf8")
        cursor = conn.cursor()
        cursor.execute('select * from member;')
        d = cursor.fetchone()
        return d


if __name__ == '__main__':
    data = MysqlData().connect_mysql()
    print(data)
