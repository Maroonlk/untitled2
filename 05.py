

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


apple = Student("apple")
bob = Student("bob")
txt = Student("txt")

print(apple.name)
print(bob.name)

print(Student.count)

class SS():
    name = "None"
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

apple = SS("apple", 18)
print(apple.name)
