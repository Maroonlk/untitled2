class A():
    def __init__(self, name):
        print("A", name)

class B(A):
    def __init__(self, name, age):
        A.__init__(self, name)
        print("B", age)

class C():
    def __init__(self, name, work):
        print("C", name, work)

class D(C):
    def __init__(self, name, work, age):
        super(D, self).__init__(name, work)
        print("D", age)


apple = B("apple", 18)
bob = D("bob", "eat", 21)

