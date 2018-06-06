class Animel(object):
    def __init__(self, name):
        print("I am Animel {0}".format(name))



class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("I am swimming......")

class Bird():
    def __int__(self, name):
        self.name = name

    def fly(self):
        print("I am flying.....")

class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("I am working.....")



class SuperMan(Animel, Person, Bird, Fish):
    pass

class Student(Person):
    pass

apple = SuperMan("apple")
apple.work()
apple.fly()
apple.swim()

bob = Student("bob")
bob.work()