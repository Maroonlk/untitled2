class Animal(object):

    def run(self):
        print("Animal is runing...")

    def eat(self):
        print("Eating meat...")


class Dog(Animal):

    def run(self):
        print("Dog is runing...")

    def eat(self):
        print("Eating meat...")


class Cat(Animal):

    def run(self):
        print("Cat is runing")


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()
cat.eat()


run_twice(Dog())

run_twice(Tortoise())

print(dir(Dog))
print(Dog.__dict__)

print("ABC".__len__())

