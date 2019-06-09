# @Time     : 2019-04-18 19:25:34
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : 本节课主要内容.py
# @function : 

"""
01.23  实战（六）
1、在common.contants添加了配置文件路径
2、在common添加了config 配置文件模块 类
3、在conf文件夹里添加了3个配置文件
4、在conmmon.request.Request类里 引入了配置文件，拼接新的url
5、修改datas.cases.xlsx里的充值表单里的url
6、在testcases.test_recharge.RechargeTest类里面执行


01.23作业
1、cases.xlsx投资表单里新增用例
管理员正常登陆
管理员加标
管理员审核
投资人正常登陆


01.26  实战（七）
1、在study_re.py学习了正则的基础用法
2、在common.contest.py写使用正则的方法


060-61_01.28：（八）反射
1、类增加属性 与 对象增加属性 区别
2、setattr(类名, key, 值) 临时增加属性
3、getattr(类名, key)  根据属性名获取属性
4、hasattr(类名, key)  判断类里是否由此值
5、common.context.py新增了一个类Context 替换配置
6、common.context.py新增了一个方法replace_new(s)  替换参数
7、在testcases.test_invest.py里面运行
8、Context，replace_new 分别引入到test_invest.py 替换测试数据
9、判断 符合条件 再 读取数据库
10、断言设置通过code码断言
11、运行结束记得加入关闭MySQL代码
12、配置文件中要加反射置换数据


062-63_0213_(实战九)
1、创建了logger日志,mango老师教的，创建my_logger回顾华华老师的
2、test_login中引入logger
3、引入新的日志模块import logging.handlers
4、模仿老师改写ddt 在libext中，可以直接显示用例名
5、test3配置文件中夹log参数化配置信息
6、common.contants里面加配置文件路径


064-65_0216_(实战十)
1、完善logger脚本
2、在request.py中引用
3、from common import contants, logger  # 引入常量 ,同时引入两个



"""