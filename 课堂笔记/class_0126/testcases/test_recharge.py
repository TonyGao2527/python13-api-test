# @Time     : 2019-04-10 21:16:26
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : test_recharge.py
# @function : 充值，期望结果只用code表示20109

# 如何获取cookie ----先学两种较简单的，后面老师教第三种最优的
# 1. 第一步 Excel 里面涉及第一条case是正常登陆
# 2. 第二步 session保持绘画的方式来进行请求的话，那就需要把你这个request的实例化的对象放到类里面
# 3. 第三步 获取Excel数据，运行用例
import unittest
from ddt import ddt, data
from common import contants
from common.do_excel import DoExcel
from common.request import Request
from common.config import ReadConfig


@ddt
class RechargeTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.read('recharge')

    @classmethod
    def setUpClass(cls):  # 每个测试类 里面取运行的操作放在类方法。一个类只一次
        print("\n这是一个setUpClass类方法\n")  # 登陆也可以放在这里做
        cls.request = Request()  # 实例化对象。为啥没传cookie，就因为这里封装request创建了会话

    def setUp(self):  # 每个测试方法 里面取运行的操作。一个方法一次
        print("这是一个setUp")
        pass

    # 引入配置文件，获取固定充值手机号
    config = ReadConfig()
    pre_investor = config.get('investor', 'mobilephone')

    @data(*cases)
    def test_recharge(self, case):
        print("开始执行第{0}条用例".format(case.case_id))

        # 引入转换格式 替换固定充实手机号
        import json
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '${investor}':
            data_dict['mobilephone'] = self.pre_investor

        resp = self.request.request(case.method, case.url, case.data)
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.json()['code'], "recharge error")  # case.text变成resp.json()字典再取code值比对。
            # 一致就写入Excel的结果位PASS，并且
            self.do_excel.write_back(case.case_id + 1, resp.text, 'PASS')
            print("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, resp.text, 'FAIL')
            print("第{0}用例执行结果：FAIL".format(case.case_id))
            raise e
        # finally:
        #     self.request.session.close()  # 不能放在finally里面，否则每次运行都关闭了

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # request封装session对话用完要关闭

# 2019.01.21 课前
"""
运行时右上角设置-播放左侧- Edit- Unitteses- 右侧Target- 选择testcases.test_recharge.RechargeTest在类下面执行，应为我们用的时ddt,指定一个方法不能生成 找不到测试类，所以选类- 点击OK

"""

