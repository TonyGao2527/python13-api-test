# @Time   : 2019-04-01 21:07:55
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : test_case.py
import requests
import unittest
from ddt import ddt, data
from common.do_excel import DoExcel
from common import contants
from common.request import Request  # 导入Request类，用get、post执行接口


do_excel = DoExcel(contants.case_file)
cases = do_excel.read('login')
print(cases)  # 读取到login里面所有数据
request = Request()  # 实例化一个对象
for case in cases:
    print(type(case.data), case.data)  # 打印类型为str
    # 入参处理
    resp = request.request(case.method, case.url, case.data)  # 调用
    print(type(resp.json), resp.json())  # dic类型
    print(type(resp.text), resp.text)  # str类型，excel里只能写入字符串
    if resp.text == case.expected:
        do_excel.write_back('login', case.case_id+1, resp.text, 'PASS')
    else:
        do_excel.write_back('login', case.case_id+1, resp.text, 'FAIL')


# 为啥这方式能运行但是不写入呢？
"""
do_excel = DoExcel(contants.case_file)
cases = do_excel.read('login')


@ddt
class Total(unittest.TestCase):

    def setUp(self):
        self.session = requests.sessions.session()

    def tearDown(self):
        print('------一条用例执行完毕------')

    @data(*cases)
    def test_case(self, case):
        case.data = eval(case.data)  # 转换一下
        print(case.data)
        if case.case_id == 'get' or case.case_id == 'GET':  # 判断请求
            resp = self.session.request('get', url=case.url, params=case.data)  # 调用
            if resp.text == case.expected:  # 比对实际结果
                do_excel.write_back('login', case.case_id+1, resp.text, 'Pass')  # 写入结论
            else:
                do_excel.write_back('login', case.case_id+1, resp.text, 'Fail')  # 写入结论
        elif case.case_id == 'post' or case.case_id == 'POST':
            resp = self.session.request('post', url=case.url, data=case.data)
            if resp.text == case.expected:
                do_excel.write_back('login', case.case_id + 1, resp.text, 'Pass')
            else:
                do_excel.write_back('login', case.case_id + 1, resp.text, 'Fail')


if __name__ == '__main__':
    unittest.main()
"""

