class Animel(object):
    def __init__(self, name):
        print("I am Animel {0}".format(name))

class Dog(Animel):
    super().__init__()