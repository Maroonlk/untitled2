class XueShen():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print(self):
        print("{0} : {1}".format(self.__name, self.__age))

    def how_is_age(self):
        if self.__age >= 18:
            print("你成年了")
        elif self.__age >= 16:
            print("快成年咯")
        elif self.__age >= 10:
            print("小学生，揍你")
        else:
            print("哇")
        return self

    def allprint(self):
        self.print()
        self.how_is_age()


class Print(XueShen):
    def allprint(self):
        self.how_is_age()


apple = XueShen("apple", 18)
bob = XueShen("bob", 17)
tw = XueShen("tw", 15)
qq = XueShen("qq", 8)

dog = Print("dog", 90)
dog.allprint()
dog.print()