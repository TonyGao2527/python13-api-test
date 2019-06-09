# @Time   : 2019-04-07 11:06:48
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : test_login.py

import unittest
from common.do_excel import DoExcel  # 引入读写类
from common.request import Request  # 引入请求类
from common import contants  # 引入常量
from ddt import ddt, data
# 一个接口一个类，一个类一个方法 #如此模块 ，100个接口100个py文件，有的接口要数据校验，有的不需要数据校验。
# 一个类，多个方法，多个接口 #如text_api.py
# 一个类，一个方法，全部接口----老师不建议后面接口会复杂，但如果接口是非常简单的调用然后判断返回，这种方式是最省事的，自己实践


@ddt
class LoginTest(unittest.TestCase):
    # 可类里，也可模块外
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.read('login')
    request = Request()  # 实例化一个对象
    # 可类里，也可模块外

    def setUp(self):
        pass

    @data(*cases)  # 此处传入数据，so读数据就要从test_login()方法移到方法外面，for case in cases:也需删掉
    def test_login(self, case):  # 加case接收解包数据
        print("开始执行第{0}行用例".format(case.case_id))
        # 使用分装好的request来完成请求
        resp = self.request.request(case.method, case.url, case.data)  # 实例对象已移到外面，这里要加self.
        # 将返回结果与期望结果对比
        # 当用unittest时,比对用断言，不用if恒等==手动了
        try:
            self.assertEqual(case.expected, resp.text, 'login error')
            # 一致就写入Excel的结果PASS
            self.do_excel.write_back(case.case_id+1, resp.text, 'PASS')  # 实例对象已放外面，类变量加self.
            print("第{0}行用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_back(case.case_id, resp.text, 'FAIL')  # 实例对象已放外面，类变量加self.调用
            print("第{0}行用例执行结果：FAIL".format(case.case_id))
            raise e

    def tearDown(self):
        pass


"""
执行的时候一定要写main函数吗？
（鼠标右键test_案例，与右键class类，运行不一样）
如何不写mai 又能去run?
Pycharm右上角播放左侧按钮点击- Edit Configurations左上角+加号- Python tests- Unitteses- 会生成一个Unnamed- 右侧Unittests里Target:选Module name执行- 点右侧三个点- 进入搜索test_login选模块而不是方法- 点OK- 顶部Name改名字为Unittests- 点右下角Apply- 再点OK- 此时运行的时候不需要鼠标右键点运行- 而是Pycharm右上角的运行播放按钮。
但这样对Unittest来说只运行了一个用例---看左下角，但实际对test_login这个方法工作台运行了6个用例。
Project: 选根目录
Python interpreter:选根目录
这俩不一样会导致运行失败，通过右上角点Unittests和在函数外点鼠标右键运行很像

基于这种方法相相实现6个用例而不是1个用例怎么办？----用ddt，再运行之后就发现左下角变6个用例了
unittest没有这功能，但ddt可再unittest基础上实现此功能

未来多个接口（多个sheet表单）是用一个TestCase执行还是用多个TestCase来执行？
"""