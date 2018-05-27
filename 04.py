class A(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def say(self):
        print("{0}, {1}".format(self.__name, self.age))




bob = A("bob", 22)
bob.say()
bob._A__name = "ad"
print(bob._A__name)  #访问私有成员

print(dir(bob))  #访问私有成员

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(obj.x + obj.x)