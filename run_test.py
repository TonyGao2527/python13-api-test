# @Time     : 2019-06-02 16:47:20
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : run_test.py
# @function : 批量运行用例，生成测试报告--mongo老师新方法

# unittest.defaultTestLoader中的discover方法：def discover(self, start_dir, pattern='test*.py', top_level_dir=None):
# start_dir是开始目录，top_level_dir是截止目录。如果只有一级目录，这俩就是相同的无需考虑。如果有多层级浅套目录，需要设置。
# pattern是正则，支持模糊匹配 * 星代表全部

# 要提前设置常量路径--contants里添加所有模块运行所在文件夹路径 testcases_dir

# HTMLTestRunnerNew放在新建子文件夹里libext，要放在项目里，跟随复制移动，因为这个模块不能自动下载安装它是华华老师自己写的


"""
# 华华老师的方式 mongo老师的新方法不需要了
import HTMLTestRunnerNew  # 引入网页报告 华华老师方法
from testcases.test_invest import InvestTest  # 引入投标类
from testcases.test_recharge import RechargeTest  # 引入充值类
from testcases.test_login import LoginTest  # 引入登陆类


suite = unittest.TestSuite()  # 测试用例集合
loader = unittest.TestLoader()  # 加载用例
suite.addTest(loader.loadTestsFromTestCase(InvestTest))
# suite.addTest(loader.loadTestsFromTestCase(RechargeTest))
suite.addTest(loader.loadTestsFromTestCase(LoginTest))
"""


import unittest
from libext import HTMLTestRunnerNew  # 引入网页报告
from common import contants


# 自动查询testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(contants.testcases_dir, pattern="test_*.py", top_level_dir=None)

with open(contants.reports_html, 'wb+') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='API', description='这是简单说明--API测试报告', tester='修宇')
    runner.run(discover)  # 执行查询到的用例
    # 还要注意替换报告路径，之前的wb变成了wb+


# 改写ddt：老师改了ddt的源码单独放在python-13-api-test/libext/ddtnew.py
"""
进入ddt源码中会看到.__dict__.这是一个字典会返回当前这个类的所有属性。
举例：print(g.__dict__)
def mk_test_name(name, value, index=0):
    index = "{0:0{1}}".format(index + 1, index_len)
    if not is_trivial(value):
        from common.do_excel import Cases  # 新增
        if isinstance(value, Cases):  # 新增
            value = value.title  # 新增
            return "{0}_{1}_{2}".format(name, index, value)  # 新增
        else:  # 新增
            return "{0}_{1}".format(name, index)

打断点：
test_login.py中下面三行分别打了断点 
    def test_login(self, case):  # 加case接收解包数据  # 断点
        logger.info("开始执行第{0}行用例".format(case.case_id))  # 断点
        # 使用分装好的request来完成请求
        resp = self.request.request(case.method, case.url, case.data)  # 断点

在ddtnew里面 打 两个断点 如下代码上，
    for name, func in list(cls.__dict__.items()):
                test_name = mk_test_name(name, getattr(v, "__name__", v), i)

运行test_login一下再点播放下面的按钮Resume Program(F9)往下走
每走一次就会运行一行excel里面的用例
每次运行观察里面的里面：
i：都增加一个数
test_name：都会变成新生成的名字
v里面都会变 分别case数据，观察title就是拼接上的名字后缀

value = value.title 是去对象里面的title字段(个人是这么理解的)
"""