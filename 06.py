class Person(object):
    name = "None"
    age = 18
    __score = 0  # 考试成绩是秘密，只要自己知道
    _petname = "sec"  # 小名，受保护的，子类可以用，但不能共用

    def sleep(self):
        print("Sleeping... ...")


class Teacher(Person):
    teacher_id = "9527"

    def make_test(self):
        print("Make_test... ...")


t = Teacher()
print(t.name)
print(t._petname)
# print(t.__score)
t.sleep()
t.make_test()
