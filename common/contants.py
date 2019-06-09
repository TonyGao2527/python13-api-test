# @Time     : 2019-04-03 22:04:59
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : contants.py
# @function : 数据路径


# from common.do_excel import DoExcel
# do_excel = DoExcel("..//datas//cases.xlsx")
# 上面在字母好用，在python13-api-test下报错，
# 这是相对路径，老师不建议，要用绝对路径

# 定义一个常量封装：  常量：文件夹路径。变量：
# 指定路径 封装常量路径
import os
"""
# 小简老师：课堂内容
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "datas")
case_file = os.path.join(data_dir, "cases.xlsx")

base_dir = os.path.abspath(__file__)  # 当前 文件 路径
base_dir = os.path.realpath(__file__)  # 芒果、华华一样

"""

# 读取测试用例文件的路径
# base_dir = os.path.dirname(os.getcwd())  # 根目录  # 结合两位老师最简方式 # getcwd()直接找根目录不靠谱，有时会越级目录
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 还是用芒果老师的
base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 华华老师的realpaht也能用
data_dir = os.path.join(base_dir, "datas")  # datas目录
case_file = os.path.join(data_dir, "cases.xlsx")  # cases.xlsx表格路径

# 获取配置文件-拼接uirl的路径
conf_dir = os.path.join(base_dir, "conf")  # conf路径
test_conf = os.path.join(conf_dir, "test.conf")  # 第一套 配置文件 路径
test2_conf = os.path.join(conf_dir, "test2.conf")  # 第二套 配置文件 路径
test3_conf = os.path.join(conf_dir, "test3.conf")  # 第三套 配置文件 路径（自己本地环境）
global_conf= os.path.join(conf_dir, "global.conf")  # 总开关 配置文件 路径

# 日志文件路径
logs_dir =os.path.join(base_dir, "logs")
python13_logs = os.path.join(logs_dir, "python13.log")

testcases_dir = os.path.join(base_dir, "testcases")  # 所有模块运行所在文件夹路径testcases

reports_dir = os.path.join(base_dir, "reports")  # reports文件夹路径
reports_html = os.path.join(reports_dir, "reports.html")  # reports.html网页报告路径


if __name__ == '__main__':
    print('我的项目根目录base_dir：', base_dir)
    print('用例excel路径', case_file)
    print('配置文件路径', test_conf)
    print('日志文件路径', python13_logs)
    print('运行模块文件夹路径', testcases_dir)
    print('网页报告路径', reports_html)

    # F:\Wenjian\Python_Pycharm\python13-api-test\conf\test.conf