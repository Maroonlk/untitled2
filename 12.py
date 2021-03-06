class Person(object):
    # 实例方法
    def eat(self):
        print(self)
        print("Eating......")
    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.....")

    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying....")

yueyue = Person()

yueyue.eat()

yueyue.play()

yueyue.say()