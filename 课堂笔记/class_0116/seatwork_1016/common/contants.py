# @Time   : 2019-04-03 22:04:59
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : contants.py


# from common.do_excel import DoExcel
# do_excel = DoExcel("..//datas//cases.xlsx")
# 上面在字母好用，在python13-api-test下报错，
# 这是相对路径，老师不建议，要用绝对路径

# 定义一个常量封装：  常量：文件夹路径。变量：
# 指定路径 封装常量路径
import os

"""
# 定义工程根目录路径，用绝对路径来写。相当于两个点..
base_dir = os.path.abspath(__file__)  # 当前 文件 路径
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test\common\contants.py
base_dir = os.path.realpath(__file__)  # 芒果、华华一样
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test\common\contants.py

base_dir = os.path.dirname(os.path.abspath(__file__))  # 文件夹 路径，相当与一个点./
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test\common
base_dir = os.path.dirname(os.path.realpath(__file__))  # 芒果、华华一样
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test\common

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 进入根目录 两个点../
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test
base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 芒果、华华一样
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test
base_dir = os.path.dirname(os.getcwd())  # 芒果、华华一样
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test

# # 路径拼接 分步
# base_dir = os.path.join(base_dir, "datas")  # 拼接到文件夹
# # 打印：F:\Wenjian\Python_Pycharm\python13-api-test\datas
# case_file = os.path.join(base_dir, "cases.xlsx")  # 拼到文件
# # 打印：F:\Wenjian\Python_Pycharm\python13-api-test\datas\cases.xlsx

# 路径拼接 一句
case_file = os.path.join(base_dir, "datas", "cases.xlsx")
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test\datas\cases.xlsx
case_file = os.path.join(base_dir+"\datas"+"\cases.xlsx")
# 打印：F:\Wenjian\Python_Pycharm\python13-api-test\datas\cases.xlsx

"""
# 小简老师：课堂内容
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "datas")
case_file = os.path.join(data_dir, "cases.xlsx")

"""

# 选取两位老师最简方式
base_dir = os.path.dirname(os.getcwd())  # 根目录
case_file = os.path.join(base_dir, "datas", "cases.xlsx")
print(case_file)
"""