# @Time     : 2019-05-18 11:54:43
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : suite_case.py
# @function : 批量运行用例，且生成网页报告

import unittest
import HTMLTestRunnerNew
from testcases.test_invest import InvestTest
from testcases.test_recharge import RechargeTest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(InvestTest))
# suite.addTest(loader.loadTestsFromTestCase(RechargeTest))
with open('python13.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='这是报告大标题--投标接口', description='这是简单说明--接口自动化第一次生成报告', tester='修宇')
    runner.run(suite)
