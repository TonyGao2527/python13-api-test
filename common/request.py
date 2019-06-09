# @Time     : 2019-04-04 23:58:39
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : request.py
# @function : 请求 引入配置url

import requests
from common.config import ReadConfig  # 引入配置文件
from common import logger  # 引入log日志模块

logger = logger.get_logger('request')  # 实例log函数并设置监听器名为request


class Request:
    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session。同一个session里cookie是共享的。

    def request(self, method, url, data=None):  # 因为共享session，所以这里不需要传cookie了

        # 引入配置文件 拼接url
        config = ReadConfig()  # 实例配置文件类
        pre_url = config.get('api', 'pre_url')  # 获取配置文件url
        url = pre_url + url  # 组成完整的url

        method = method.upper()  # 将字符串全改成大写，兼容性
        if data is not None and type(data) == str:
            data = eval(data)  # 如果是字符串需转字典。否则运行结果为：...'手机号码不能为空'
        logger.info('method：{0}  url：{1}'.format(method, url))
        logger.info('data：{0}'.format(data))

        if method == 'GET':
            # return self.session.request(method, url=url, params=data)  # 注意方式params，data要传字典
            resp = self.session.request(method, url=url, params=data)
            logger.info('response：{0}'.format(resp.text))
            return resp
        elif method == 'POST':
            # return self.session.request(method, url=url, data=data)  # 注意方式data，data要传字典
            resp = self.session.request(method, url=url, data=data)
            logger.info('response：{0}'.format(resp.text))
            return resp
        else:
            logger.error('Un-support method !!!')

    def close(self):
        self.session.close()  # 关闭session