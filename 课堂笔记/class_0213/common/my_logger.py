# @Time     : 2019-05-16 20:39:22
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : my_logger.py
# @function : 整理华华的log代码

# 封装日志类
from common.config import ReadConfig  # 引入 配置文件类
from common import contants  # 引入文件路径类
import logging


class MyLog:
    def __init__(self):
        config = ReadConfig()
        self.in_level = config.get('log', 'in_level')
        self.out_level = config.get('log', 'out_level')
        self.file_level = config.get('log', 'file_level')
        self.formatter = config.get('log', 'formatter')

    def my_log(self, level, msg):
        my_logger = logging.getLogger("python13")  # 创建日志收集器
        my_logger.setLevel(self.in_level)  # 收集器级别
        formatter = logging.Formatter(self.formatter)
        ch = logging.StreamHandler()  # 指定输出控制台
        ch.setLevel(self.out_level)  # 控制台输出级别
        ch.setFormatter(formatter)  # 设置输出格式
        fh = logging.FileHandler(contants.python13_logs, encoding='utf-8')  # 指定输出到文件
        fh.setLevel(self.file_level)  # 文件输出级别
        fh.setFormatter(formatter)  # 只是输出格式
        my_logger.addHandler(ch)  # 控制台对接
        my_logger.addHandler(fh)  # 文件对接
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        my_logger.removeHandler(ch)  # 去掉重复日志，移除日志收集器
        my_logger.removeHandler(fh)  # 去掉重复日志，移除日志收集器

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug('作业啥时候能完成？')
    # 打印：2019-05-18 11:29:04,829-[DEBUG]-[my_logger.py]-[line:34]-[收集器名字：python13]-[日志信息]:作业啥时候能完成？








