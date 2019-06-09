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

"""
# 结合两位老师最简方式
# 读取测试用例文件的路径
base_dir = os.path.dirname(os.getcwd())  # 根目录
data_dir = os.path.join(base_dir, "datas")  # datas目录
case_file = os.path.join(data_dir, "cases.xlsx")  # cases.xlsx表格路径

# 获取配置文件-拼接uirl的路径
conf_dir = os.path.join(base_dir, "conf")  # conf路径
test_conf = os.path.join(conf_dir, "test.conf")  # 第一套 配置文件 路径
test2_conf = os.path.join(conf_dir, "test2.conf")  # 第二套 配置文件 路径
test3_conf = os.path.join(conf_dir, "test3.conf")  # 第三套 配置文件 路径（自己本地环境）
global_conf= os.path.join(conf_dir, "global.conf")  # 总开关 配置文件 路径

print(case_file)
print(test_conf)
# F:\Wenjian\Python_Pycharm\python13-api-test\conf\test.conf