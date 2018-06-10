class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = int(age)

    def __call__(self):
        print(self.name)
        print(self.age)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError

    def get_age(self):
        return self._age

    def set_age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError
    
    age = property(fget=get_age, fset=set_age, fdel=None, doc="This for age")


apple = Person("apple", 18.9)

apple()
    






class Student(object):
    def __init__(self, name):
        self._name = name
    
    def __gt__(self, obj):
        print("哈哈， {0} 会比 {1} 大吗？".format(self._name, obj._name))
        return self._name > obj._name

stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)
# print(stu1.__name__)