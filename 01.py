"""
定义一个学生，用来形容学生
"""


# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
mingyue = Student()


# 定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomeWork的缩进层级
    # 2. 系统默认有一个self参数

    def doHomeWork(self):
        print("I do homework")
        # 推荐在函数末尾使用return语句
        return None


# 实例化一个叫apple的学生， 是一个具体的人
apple = PythonStudent()
print(apple.name)
print(apple.age)
# 注意成员数据的调用，没有传递进入参数
apple.doHomeWork()

print(PythonStudent.__dict__) # 显示类的所有成员


class MyStudent():
    name = "apple"
    age = 18
    def say_hi(self):
        print('hi')
        return None

a = MyStudent()
a.name = 'Bob'
a.favorites = 'just do it'

print(a.name, a.age)
print(a.__dict__)
print(a.say_hi())

