# @Time   : 2019-04-04 23:58:39
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : request.py

import requests


class Request:
    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session。同一个session里cookie是共享的。

    def request(self, method, url, data=None):  # 因为共享，所以这里不需要传cookie了
        method = method.upper()  # 将字符串全改成大写，兼容性

        if data is not None and type(data) == str:
            data = eval(data)  # 如果是字符串需转字典。否则运行结果为：...'手机号码不能为空'
        print('method：{0}  url：{1}'.format(method, url))
        print('data：{0}'.format(data))

        if method == 'GET':
            # return self.session.request(method, url=url, params=data)  # 注意方式params，data要传字典
            resp = self.session.request(method, url=url, params=data)
            print('response：{0}'.format(resp.text))
            return resp
        elif method == 'POST':
            # return self.session.request(method, url=url, data=data)  # 注意方式data，data要传字典
            resp = self.session.request(method, url=url, data=data)
            print('response：{0}'.format(resp.text))
            return resp
        else:
            print('Un-support method !!!')


