# from enum import Enum
#
# Month = Enum("Month", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
#
# for name, member in Month.__members__.items():
#     print(name, "=>", member, ",", member.value)
#
# from enum import Enum, unique
#
# @unique
# class Weekday():
#     sun = 0
#     mon = 1
#     tue = 2
#
# day1 = Weekday.sun
# print(day1)
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')