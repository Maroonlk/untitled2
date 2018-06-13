# 自己组装一个类

class A():
    pass


def say(self):
    print("Saying... ...")


say(9)

A.say = say

a = A()
a.say()

# 函数名可以当变量使用
# 即可以使用等号


#组装类例子 2
from types import MethodType

class B():
    pass

def say(self):
    print("11111")

a = A()
a.say = MethodType(say, A)
a.say()


# 利用type

def say(self):
    print("11")

def talk(self):
    print("22")

#使用type来创建一个类

A = type("A", (object, ), {"class_say":say, "class_talk":talk})

print(A.__name__)
a = A()

a.class_say()