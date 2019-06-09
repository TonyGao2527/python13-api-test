# @Time     : 2019-04-30 23:14:36
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : test_invest.py
# @function : 

import unittest  # 引入测试方法
from common.do_excel import DoExcel  # 读取数据类
from common import contants  # 获取文件路径
from common.request import Request
from ddt import ddt, data  # 引入ddt使案例一次传入
from common import context  # 引入正则查找替换模块，含替换类、正则方法
import json
from common.mysql import MysqlUtil  # 引入读数据库值的类 下面查标id用
from common.context import Context  # 引入替换的类


@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.read('invest')

    @classmethod
    def setUpClass(cls):  # 每个测试 类 里面去运行的操作放到类方法里面，执行所有用例前只运行一次。
        print("\n这是一个类方法")
        cls.request = Request()  # 实例化对象
        # cls.mysql = MysqlUtil()  # 创建一个mysql实例且每个setUp都用这一个实例，所以放setUpClass()里面

    def setUp(self):  # 每个测试 方法 里面去运行的操作放到类方法里面，执行每一条用例前都运行一次。
        print("这是一个setUp")
        self.mysql = MysqlUtil()

    @data(*cases)
    def test_invest(self, case):
        print("开始执行第{0}行用例".format(case.case_id))
        print('Expected：', case.expected)  # 查看期望结果

        # 查找参数化的测试数据，动态替换。上面引入替换模块。正则引入替换数据
        data_new = context.replace_new(case.data)  # 传入从Excel里面读取出来的str类型的测试数据。要重新赋值data_new

        # 使用封装的request来完成请求
        resp = self.request.request(case.method, case.url, data_new)

        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(json.loads(case.expected)['code'], resp.json()['code'], 'invest error')  # resp.text改成resp.json()['code'] 只通过code判断
            # 一致就写入Excel结果为PASS，并且
            self.do_excel.write_back(case.case_id + 1, resp.text, 'PASS')

            print("第{0}行用例执行结果：PASS".format(case.case_id))

            # 加标后的标id不能直接配置文件替换，需要到数据库查询，而且根据借款人的memberID查询加成功的标loan_id
            # setUpClass()里面创建实例对象
            # 引入mysql模块中的MysqlUtil类
            # 在tearDownClass()里添加关闭，数据库用完必须关
            # 还要引入Context类 进行替换
            # 判断是否加标成功，如果成功过就按照借款人ID去数据库拆线呢最新标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                print('loan_member_id的取值：', type(loan_member_id), loan_member_id)
                sql = "SELECT Id FROM future.loan WHERE MemberID={0} ORDER BY CreateTime DESC LIMIT 1;".format(loan_member_id)  # 注意：表名loan前面必须加数据库名future.loan否则会报错(1046, 'No database selected')
                # 创建sql语句。注意：没有分号。
                loan_id = self.mysql.fetch_one(sql)[0]  # 传入sql查询得到一个元组，再取第[0]个值是int类型，再赋值
                print('self.loan_id的取值：', type(loan_id), loan_id)
                setattr(Context, 'loan_id', str(loan_id))  # 函数：给类或实例对象动态的去添加属性或者方法。
                # 注意：后面的loan_id是int类型需要转换成str类型，context.replace_new.value和key需要时str类型 否则后续正则替换会报错。使用魔术方法 动态添加load_id。
        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, resp.text, 'FAIL')
            print("第{0}行用例执行结果：FAIL".format(case.case_id))
            raise e

    def tearDown(self):
        self.mysql.close()

    @classmethod
    def tearDownClass(cls):
        # cls.request.close()  # 关闭session  # 这个没有打开会报错，但老师视频里面有
        # cls.mysql.close()  # 关闭MySQL，用完就要去关闭，否则资源一直被占用 后面的连接人就会被拒绝再连
        pass


# if __name__ == '__main__':
#     mysql = MysqlUtil()  # 创建一个mysql实例且每个setUp都用这一个实例，所以放setUpClass()里面
#     # loan_member_id = getattr(Context, 'loan_member_id')
#     sql = "SELECT Id FROM loan WHERE MemberID={0} ORDER BY CreateTime DESC LIMIT 1;".format(loan_member_id)
#     # 创建sql语句。注意：没有分号。
#     loan_id = mysql.fetch_one(sql)[0]  # 传入sql查询得到一个元组，再取第[0]个值是int类型，再赋值
#     # setattr(Context, 'loan_id', str(loan_id))  # 函数：给类或实例对象动态的去添加属性或者方法。
#     mysql.close()  # 关闭MySQL，用完就要去关闭，否则资源一直被占用 后面的连接人就会被拒绝再连
#
#     print(loan_id)
