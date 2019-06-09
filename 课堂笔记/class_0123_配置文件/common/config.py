# @Time     : 2019-04-16 19:25:31
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : config.py
# @function : 配置文件类


import configparser  # 引入解析文件方法
from common import contants

# # 实例化对象
# config = configparser.ConfigParser()  # 对象一定要有括号
# # 加载文件
# config.read(contants.global_conf, encoding='utf-8')
# # 老师的 有两个配置文件用getboolenn()
"""
open = config.getboolean('switch', 'open')  # True,False是布尔值所以要转化getboolean()
print(type(open), open)
if open:
    config.read(contants.test_conf, encoding='utf-8')  # open是True
else:
    config.read(contants.test2_conf, encoding='utf-8')  # open是False
"""
# # 自己的 有三个配置文件用get()
# open = config.get('switch_2', 'open')
# print(type(open), open)
# if open == 'test':
#     config.read(contants.test_conf, encoding='utf-8')
# elif open == 'test2':
#     config.read(contants.test2_conf, encoding='utf-8')
# elif open == 'test3':
#     config.read(contants.test3_conf, encoding='utf-8')
#
# # 以上的代码是反复用到的，选不同的配置像，不同的rul，不同的数据库信息，每次用到都需要加载，所以要写一个类class ReadConfig
#
# value = config.get('api', 'pre_url')
# print(type(value), value)  # 字符串类型的url
# # 打印：<class 'str'> http://test.lemonban.com/futureloan/mvc/api

'''
为啥用多个配置文件test1、test2、test3...？
1、多套环境，多个文件，看着更清晰直观。
2、读取的时候 代码中action和option名字不用更改。
3、还要一个总开关
'''


class ReadConfig:

    def __init__(self):
        # 实例化对象
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_conf, encoding='utf-8')  # 写死 不需要参数化
        open = self.config.get('switch_2', 'open')
        if open == 'test':
            self.config.read(contants.test_conf, encoding='utf-8')
        elif open == 'test2':
            self.config.read(contants.test2_conf, encoding='utf-8')
        else:
            self.config.read(contants.test3_conf, encoding='utf-8')

    # 放在初始化里的好处，是创建实例的时候会自动被调用执行

    def get(self, section, option):
        return self.config.get(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)  # 要有返回值，没有将获取不到。

    # data.json表格里的url前半部分都删掉，修改Request类里面的url


if __name__ == '__main__':
    read_config = ReadConfig()
    print(read_config.get('api', 'pre_url'))
