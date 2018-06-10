class KeHu(object):

    def __init__(self, name, age, phone_number=None):
        self._name = name.upper()
        self._age = int(age)
        self._phone_number = phone_number

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = int(value)

    age = property(fget=get_age, fset=set_age, fdel=None,
                   doc="This property for age")

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value.upper()

    name = property(fget=get_name, fset=set_name,
                    fdel=None, doc="This property for name")


a1 = KeHu("apple", 18.009, None)

a1.name = "bob"
print(a1.name)
print(a1.age)
print(a1._phone_number)
