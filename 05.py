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


class Mod(object):
    # __slots__ = ("name", "age")   # 限制对象所能拥有的属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("Hi, I am {0} and I'm {1} year old.".format(self.name, self.age))


apple = Mod("apple", 18)

apple.say()

print(setattr(apple, "name2", "ap"))  # 设置一个"name"的属性，值为"ap"
print(apple.name2)


class Screen(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError ("Try again")
        self._width = value

    @property
    def height(self):
        return self._height

apple = Screen(12, 1)
apple.width = 9
print(apple.width)
# apple.height = 10
print(apple.height)

































