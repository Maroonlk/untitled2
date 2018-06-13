# 元类的写法是固定的，他必须继承与type
# 元类一般命名以MetaClass结尾


class TulingMetaClass(type):
    #注意以下写法

    def __new__(cls, name, bases, attrs):
        # 自己的业务代码
        print("嘿！")
        attrs["ID"] = "000000"
        attrs["Addr"] = "address"
        return type.__new__(cls, name, bases, attrs)


# 元类定义完就可以使用， 使用注意写法

class Teacher(object, metaclass=TulingMetaClass):
    pass

t = Teacher()

t.__dict__
print(t.ID)
