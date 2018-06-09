class Person(object):
    '''
    property装饰器的用法
    分两种
    '''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            return ValueError("ValueError")


p1 = Person("apple", 17)
print(p1.get_name())
p1.set_name("bob")
print(p1.get_name())
print(Person.__doc__)


class Student(object):
    '''
    property的第一种用法
    '''
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("VE")


s1 = Student("apple")
print(s1.name)
s1.name = "bob"
print("*" * 30)

class Animel(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def fget(self):
        return self.__name

    def fset(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError

    def fdel(self):
        self.__name = "None"

    name = property(fget, fset, fdel, "对name进行操作")

a1 = Animel("Pig", 8)
print(a1.name)
a1.name = "apple"
print(a1.name)

a1.fdel()
print(a1.name)