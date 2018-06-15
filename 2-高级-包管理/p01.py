# 包含一个学生类，
# 一个sayhello函数，
# 一个打印语句

class Student(object):
    def __init__(self, name="None", age=18):
        self.name = name
        self.age = age
        print("02")

    def say(self):
        print("My name is {0}.".format(self.name))


def sayHello():
    print("Hi, 欢迎来到我的国度！")


print("我是模块p01") # 模块里最好不要有这种类似的代码
                    # 因为在导入时就会被执行


