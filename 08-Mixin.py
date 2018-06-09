# Mixin案例

class Person():
    name = "apple"
    age = 18

    def eat(self):
        print("EAT......")

    def drink(self):
        print("DRINK......")

    def sleep(self):
        print("SLEEP......")

class Teacher(Person):
    def work(self):
        print("work")

class Student(Person):
    def study(self):
        print("study")

class Tutor(Teacher, Student):
    pass


class TeacherMixin():
    def work(self):
        print("work")

class StudentMixin():
    def study(self):
        print("study")


class TutorMixin(Person, TeacherMixin, StudentMixin):
    pass

t = TutorMixin()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

help(delattr)