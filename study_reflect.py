# @Time     : 2019-04-28 20:44:25
# @Author   : lemon_xiuyu
# @Email    : 5942527@qq.com
# @File     : study_reflect.py
# @function : 反射基础

"""
魔法一样
静态---运行前，如果要调用类的属性或者方法，我需要实例画他的对象
动态---运行时，我就获取类的属性或者方法，甚至更改它的属性或者方法
"""


class Girls:

    single = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def singe(self):
        print(self.name + "会唱歌")


if __name__ =='__main__':
    # 实例化调用
    g = Girls('mongo', 18)
    print(g.name)
    g.singe()
# 打印：mongo
# 打印：mongo会唱歌

# #     print(g.hub)
# # # 报错：AttributeError: 'Girls' object has no attribute 'hub'
#     setattr(g, 'hub', 'swimming')  # 函数：给类或实例对象动态的去添加属性或者方法
#     print(g.hub)
# # 打印：swimming
#     # 添加属性前会报错，添加属性后print()可正常打印
#
#     # 把setattr()中实例g换成类名Girls有啥区别？
#     g2 = Girls('lucy', 20)
#     print(g2.hub)
# # 报错：AttributeError: 'Girls' object has no attribute 'hub'

    # 注意：实例对象g添加的，它的属性作用于仅限于当前设置的实例对象g，g的属性只能g用，g2则没有
    # 如果想g2也能用咋办？
    # g添加属性的时候用setattr()中g换成Girls
    setattr(Girls, 'hub', 'swimming')  # 函数：给类或实例对象动态的去添加属性或者方法
    # print(g.hub)

#     g2 = Girls('lucy', 20)
#     print(g2.hub)
# # 打印：swimming
# # 打印：swimming
    # 如果想给类添加属性就添加类名，后面的实例包含。如果只想给当前对象添加属性就传实例对象，后面实例都没有

    # 不想有实例化过程，想直接根据属性名获取值咋弄？
    # 用getattr()。后面不同module不同类之间传递用的方法就是setattr()和getattr()
    print(getattr(Girls, 'hub'))  # 根据属性名获取类的属性，当属性不存在的时候，报AttributeError
# 打印：swimming
    # 不需要实例化，注释掉只用setattr()和getattr()依然能获取到hub属性值

#     # 获取没有传值也没有定义的属性会怎样？
#     print(getattr(Girls, 'male'))
# # 报错：AttributeError: type object 'Girls' has no attribute 'male'

    # 加标用例失败了，会报错，会影响下一个投资用例也失败。这里可加一个判断，如果加标案例失败则直接终止
    # 如何判断是否有loadid是否有属性？----hasattr()
    print(hasattr(Girls, 'male'))  # 判断当前这个类有没有这个属性，有就返回True，没有就返回False 不会报错。
# 打印：False
    print(hasattr(Girls, 'name'))  # 上面__init__()初始化里有，但是通过类找不到
# 打印：False
    print(hasattr(Girls, 'single'))  # 判断是否有类属性，single实在初始化外面，属于类属性
# 打印：True
    print(hasattr(g, 'name'))  # 判断对象是否有这个实例属性，上面的对象有打开了
# 打印：True

#     # 动态删除某个属性。用完之后不想让这个实例再有此属性了。前面的时候需要用，后面又想清零
#     delattr(g, 'name')  # 删除对象属性
#     print(g.name)
# # 报错：AttributeError: 'Girls' object has no attribute 'name'

    # 是否可以删除Girls类属性呢？
    delattr(Girls, 'single')  # 删除类属性
    print(Girls.single)
# 报错：AttributeError: type object 'Girls' has no attribute 'single'

# 要解决一个什么样的场景？
# 多个方法之间的数据传递
# 多个类之间多个module之间传递数据,动态添加方法、属性
# setattr()可以传递方法，只要把方法名传进去

# 配置文件里面怎加一个section名字为[data] , admin_user =
# 在common- context.py- 新建一个类class Context:
# 在赋值def replace(s, d):方法为def replace_new(s): ，新方法里面不传字典
# 加 getattr(类，属性)
# 加if判断
# 加标成功后审核时的${loand_id}需要根据加成功的标来查，所以loand_id不需要定义成类属性

    print(g.__dict__)  # 打印G的所有属性
