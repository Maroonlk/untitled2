class Teacher():
    name = "None"
    age = 18

    def sayHi(self):
        self.name = "apple"
        self.age = 23
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    def saytwo():
        print(__class__.name)
        print(__class__.age)
        print("Hi, see you again")

pop = Teacher()
pop.sayHi()
Teacher.saytwo()

class A():
    name = "liuying"
    age = 18

    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = 90

