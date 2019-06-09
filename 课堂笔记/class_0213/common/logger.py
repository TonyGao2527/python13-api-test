# @Time     : 2019-05-19 17:09:05
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : logger.py
# @function : mongo老师的log新方法

import logging  # 华华老师教的方法
import logging.handlers  # 芒果老师的新方法
from common import contants  # 引入根目录文件
import os  # 引入拼接


# 输出到文件，文件路径请使用绝对路径 logs目录下
# 输出到控制台，定义输出级别是debug
# 不同的输出级别可配置


def get_logger(logger_name):  # 通过函数进行封装
    logger = logging.getLogger(logger_name)  # 实例化，创建监听器，不输入名字默认的是root。不同的log定义不同的名字，如投标'invest',封装后要参数化,在生成的日志里面更容易区分是哪个模块生成的日志。
    logger.setLevel('INFO')
    # logger.error('eeeee')  # 直接打印默认输出控制台
    # logger.info('iiiii')   # 直接打印默认过滤掉error以下级别
    # 定义输出格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"  # 源码里就有各个格式的标注
    formate = logging.Formatter(fmt)  # 定义日志格式
    # 创建日志文件绝对路径
    file_name = os.path.join(contants.logs_dir, 'case.log')
    # 输出到文件 新方法：定义最大字节数，以及备份次数
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20 * 1024 * 1024, backupCount=10, encoding='utf-8')  # 输出到文件。 maxBytes是最大字节数，backupCount是备份次数
    file_handler.setLevel('INFO')  # 输出文件级别 info以上的输出，以下的就不传了不占用资源
    file_handler.setFormatter(formate)  # 设置输出文件格式
    logger.addHandler(file_handler)  # 建立连接，不然logger不知道输出格式。

    return logger  # 封装后最后返回log


if __name__ == '__main__':
    logger = get_logger(logger_name='invest')
    logger.error('this is error')

# 写入日志：2019-05-20 01:40:15,262 - invest - ERROR - eeeee - [logger.py:23]

# 写入日志：2019-05-20 01:51:32,710 - invest - ERROR - this is error - [logger.py:29]

# 在test_login 模块引入日志

# 注意：file_handler文件输出里面的文件名是 绝对路径，那不同文件夹下的模块引用会导入同一个log文件种。文件输出里的文件名是 相对路径，那么不同文件夹下的脚本调用会分别生成log文件，所有的不在一起。所以需要用绝对路径。