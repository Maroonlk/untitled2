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
    def say_hi(self, age = 8):
        self.naem = 'aaaa'
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(age))
        return None

a = MyStudent()
a.name = 'Bob'
a.favorites = 'just do it'

print(a.name, a.age)
print(a.__dict__)
a.say_hi()

class Teacher():
    name = "Apple"
    age = 19

    def say(self):
        self.name = "Bob"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    def sayagain():
        print(__class__.name)
        print(__class__.age)
        print("Hello, nice to see you again!")

t = Teacher()
t.say()
Teacher.sayagain()          # 调用绑定类的函数使用类名

#0603
