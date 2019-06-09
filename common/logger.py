# @Time     : 2019-05-19 17:09:05
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : logger.py
# @function : mongo老师的log新方法

import logging  # 华华老师教的方法
import logging.handlers  # 芒果老师的新方法
import os  # 引入拼接
from common import contants  # 引入根目录文件
from common.config import ReadConfig


# 输出到文件，文件路径请使用绝对路径 logs目录下
# 输出到控制台，定义输出级别是debug
# 不同的输出级别可配置
config = ReadConfig()  # 实例化配置文件


def get_logger(logger_name):  # 通过函数进行封装
    logger = logging.getLogger(logger_name)  # 实例化创建监听器，名字默认的是root
    logger.setLevel('INFO')  # 监听器级别，直接设最低，写死不需配置
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"  # 定义日志格式
    formate = logging.Formatter(fmt)  # 定义日志格式，Formatter里有格式

    file_name = os.path.join(contants.logs_dir, 'case.log')  # 读取配置文件-输出文件路径
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20 * 1024 * 1024, backupCount=10, encoding='utf-8')  # 输出到文件。 maxBytes是最大字节数，backupCount是备份次数
    level = config.get('log', 'file_handler')  # 读取配置文件-输出文件级别
    file_handler.setLevel(level)  # 输出文件级别
    file_handler.setFormatter(formate)  # 设置输出文件格式

    console_handler = logging.StreamHandler()  # 输出到控制台
    level = config.get('log', 'console_handler')  # 读取配置文件-输出控制台级别
    console_handler.setLevel(level)  # 输出控制台姐别
    console_handler.setFormatter(formate)  # 设置输出控制台格式

    logger.addHandler(file_handler)  # 输出到文件建立连接，放到总logger里，不然logger不知道输出格式。
    logger.addHandler(console_handler)  # 输出到控制台建立连接

    return logger  # 封装后最后返回log


if __name__ == '__main__':
    logger = get_logger(logger_name='invest')
    logger.error('this is error')
    logger.info('this is info')
    logger.debug('this is debug')
    # 控制台输出：2019-05-22 21:31:25,275 - invest - ERROR - this is error - [logger.py:45]  # 控制台过滤error以下
    # 文件输出：2019-05-22 21:31:25,275 - invest - ERROR - this is error - [logger.py:45]
    # 文件输出：2019-05-22 21:31:25,296 - invest - INFO - this is info - [logger.py:46]  # 文件过滤info以下
    print(contants.testcases_dir)