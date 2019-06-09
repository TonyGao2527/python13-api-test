# @Time   : 2019-04-07 16:36:06
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : test_api.py

import unittest
from common.do_excel import DoExcel  # 引入读写类
from common.request import Request  # 引入请求类
from common import contants  # 引入常量
from ddt import ddt, data
from common.mysql import MysqlUtil  # 引入数据库

"""
注册成功接口数据每次都手动修改未注册过的很麻烦，怎么破？
1，数据库里面查最大的手机号+1（或138里面最大的）
2，将case.data里面的手机号码给替换掉
3，然后再去请求
"""


@ddt
class APITest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    login_cases = do_excel.read('login')  # 一个就够，不需要重复写多个对象
    request = Request()  # 实例化一个对象

    def setUp(self):
        pass

    @unittest.skip("忽略测试，不要运行")  # 暂时不运行此用例
    @data(*login_cases)
    def test_login(self, case):
        print("开始执行第{0}行用例".format(case.case_id))
        # 使用分装好的request来完成请求
        resp = self.request.request(case.method, case.url, case.data)  # 实例对象已移到外面，这里要加self.
        # 将返回结果与期望结果对比
        try:
            self.assertEqual(case.expected, resp.text, 'login error')
            # 一致就写入Excel的结果PASS
            self.do_excel.write_back(case.case_id+1, resp.text, 'PASS')  # 实例对象已放外面，类变量加self.
            print("第{0}行用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_back(case.case_id+1, resp.text, 'FAIL')  # 实例对象已放外面，类变量加self.调用
            print("第{0}行用例执行结果：FAIL".format(case.case_id))
            raise e

    register_cases = do_excel.read('register')  # 增加了一个方法

    # mysql = MysqlUtil()  # 实例化对象（进行了一次数据库的连接）
    # sql = "SELECT MAX(MobilePhone) FROM future.member WHERE MobilePhone LIKE '152%';"  # 传一条sql进来
    # max = mysql.fetch_one(sql)[0]  # 找到最大手机号码, 元组里取第1个值
    # print(type(max), max)

    @data(*register_cases)
    def test_register(self, case):

        mysql = MysqlUtil()  # 实例化对象（进行了一次数据库的连接）
        sql = "SELECT MAX(MobilePhone) FROM future.member WHERE MobilePhone LIKE '152%';"  # 传一条sql进来
        max = mysql.fetch_one(sql)[0]  # 找到最大手机号码, 元组里取第1个值

        print("开始执行第{0}行用例".format(case.case_id))
        import json
        data_dict = json.loads(case.data)  # Excel字符串转成字典
        if data_dict['mobilephone'] == '${register_mobile}':  # 判断是否等于标记
            data_dict['mobilephone'] = int(max) + 1  # 将最大手机号码+1 赋值给mobilephone

        # 使用封装好的request来完成请求
        resp = self.request.request(case.method, case.url, data_dict)  # 实例对象已移到外面，这里要加self.
        # 将返回结果与期望结果对比
        try:
            self.assertEqual(case.expected, resp.text, 'register error')
            # 一致就写入Excel的结果PASS，并且
            self.do_excel.write_back(case.case_id+1, resp.text, 'PASS')  # 实例对象已放外面，类变量加self.
            print("第{0}行用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_back(case.case_id+1, resp.text, 'FAIL')  # 实例对象已放外面，类变量加self.调用
            print("第{0}行用例执行结果：FAIL".format(case.case_id))
            raise e

    def tearDown(self):
        pass


"""
Pycharm右上角播放左侧按钮- Edit Configurations- 左上角Unittests进行修改- 右侧Targer选Module name右侧...三点搜索test_register- Project: 选根目录(python13-api-test)- Python interpreter:选根目录(python13-api-test)- Apply- OK
然后 右上角Unittests运行 结果报错：AttributeError: type object 'APITest' has no attribute 'test_register'

为什么呢？
这是属性报错，相当于直接在test_register方法上鼠标右键运行。
ddt在寻找的时候，必须先找到测试类，然后再去找测试方法，帮助在测试类里面去生成测试方法。
如何解决？
Pycharm右上角播放左侧按钮- Edit Configurations- 将Unittest- Targer选Module name右侧...三点中的test_register改成test_api 再点pycharm右上角运行
全部login、register案例运行成功，相当于鼠标右键函数名运行。

用ddt单独执行某一个用例，就不行了。
老师后面会讲：0128日志处理与报告生成
"""