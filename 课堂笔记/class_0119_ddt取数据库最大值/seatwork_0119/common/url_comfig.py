# @Time   : 2019-04-09 23:52:49
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : url_comfig.py

# 拼接URL 0119课后作业 自己练习的
from configparser import ConfigParser
from common import contants


class ReadConfig:
    def __init__(self, file):
        self.cf = ConfigParser()
        self.cf.read(file, encoding='utf-8')

    def get_value(self, section, option):
        result = self.cf.get(section, option)
        return result


if __name__ == '__main__':
    res = ReadConfig(contants.case_config).get_value('UrlChange', 'url_1')
    print(res)
# F:\Wenjian\Python_Pycharm\python13-api-test\conf\case.conf
# contants.case_config
