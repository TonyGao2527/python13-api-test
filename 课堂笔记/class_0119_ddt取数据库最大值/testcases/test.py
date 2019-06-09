# @Time   : 2019-04-03 21:59:06
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : test.py

from common.do_excel import DoExcel
from common import contants
from common.request import Request  # 导入Request类，用get、post执行接口

# 接口自动化流程 写用例--执行用例--报告
do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
cases = do_excel.read('login')
request = Request()  # 实例化一个对象
for case in cases:
    print("开始执第{0}行用例".format(case.case_id))
    # 使用封装好的request 来完成请求
    resp = request.request(case.method, case.url, case.data)  # 调用
    # 将返回结果和期望结果进行匹配
    if resp.text == case.expected:
        # 一致就写入Excel的结果为PASS,并且
        do_excel.write_back(case.case_id+1, resp.text, 'PASS')
        print("第{0}行用例执行结果：PASS".format(case.case_id))
    else:
        do_excel.write_back(case.case_id+1, resp.text, 'FAIL')
        print("第{0}行用例执行结果：FAIL".format(case.case_id))
