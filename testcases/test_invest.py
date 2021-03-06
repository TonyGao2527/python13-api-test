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
from common import context, logger  # 引入正则查找替换模块，含替换类、正则方法
import json
from common.mysql import MysqlUtil  # 引入读数据库值的类 下面查标id用
from common.context import Context  # 引入替换的类
# from common import logger

logger = logger.get_logger(logger_name='invest')  # 获取logger实例


@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.read('invest')

    @classmethod
    def setUpClass(cls):  # 整个类开始执行前执行，且只一次
        logger.debug("\n这是一个类方法")
        cls.request = Request()  # 实例化请求对象
        # cls.mysql = MysqlUtil()  # 创建一个mysql实例，每个setUp()都用这个实例，所以放在classmethod()里就只建一次，提高性能

    def setUp(self):  # 每个测试方法的每一个用例运行前都要执行一遍的放在这里，这一次代替里面的多次
        logger.debug("这是一个setUP")
        # self.mysql = MysqlUtil()  # 整个类只执行一次，后面相同用例不能覆盖，需要每个用例都要执行，所以还是要放在这里

    @data(*cases)
    def test_invest(self, case):
        logger.info("开始执行第{0}行用例".format(case.case_id))
        logger.info('Expected：{0}'.format(case.expected))  # 查看期望结果

        # 查找参数化数据，动态替换
        data_new = context.replace_new(case.data)  # Str测试数据

        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_new)

        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(json.loads(case.expected)['code'], resp.json()['code'],
                             'invest error')  # resp.text改成resp.json()['code'] 只通过code判断
            # 一致就写入Excel结果为PASS，并且
            self.do_excel.write_back(case.case_id + 1, resp.text, 'PASS')
            logger.info("第{0}行用例执行结果：PASS".format(case.case_id))

            # 加标后的标id不能直接配置文件替换，需要到数据库查询，而且根据借款人的memberID查询加成功的标loan_id
            # setUpClass()里面创建实例对象
            # 引入mysql模块中的MysqlUtil类
            # 在tearDownClass()里添加关闭，数据库用完必须关
            # 还要引入Context类 进行替换
            # 判断是否加标成功，如果成功过就按照借款人ID去数据库拆线呢最新标的记录
            if resp.json()['msg'] == '加标成功':
                mysql = MysqlUtil()
                loan_member_id = getattr(Context, 'loan_member_id')
                logger.debug('loan_member_id的取值：{0}{1}'. format(type(loan_member_id), loan_member_id))
                sql = "SELECT Id FROM future.loan WHERE MemberID={0} ORDER BY CreateTime DESC LIMIT 1;".format(
                    loan_member_id)  # 注意：表名loan前面必须加数据库名future.loan否则会报错(1046, 'No database selected')
                # 创建sql语句。注意：没有分号。
                loan_id = mysql.fetch_one(sql)[0]  # 传入sql查询得到一个元组，再取第[0]个值是int类型，再赋值
                logger.debug('self.loan_id的取值：{0}{1}'. format(type(loan_id), loan_id))
                setattr(Context, 'loan_id', str(loan_id))  # 函数：给类或实例对象动态的去添加属性或者方法。
                # 注意：后面的loan_id是int类型需要转换成str类型，context.replace_new.value和key需要时str类型 否则后续正则替换会报错。使用魔术方法 动态添加load_id。
                mysql.close()
        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, resp.text, 'FAIL')
            logger.error("断言出错了：{}".format(e))
            logger.error("第{0}行用例执行结果：FAIL".format(case.case_id))
            raise e

    def tearDown(self):
        # self.mysql.close()  # 关闭MySQL 防止资源被占用
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.close()  # 关闭session  # 这个没有打开会报错，但老师视频里面有
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
