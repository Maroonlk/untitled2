import random
'''
此程序生成一个4 x 4的包含阿拉伯数字和26个不区分大小写字母的激活码
例： 12Df7-V8Fd1-mg8Yr-s9IkJ 
'''
class JiHuoMa(object):
    def __init__(self, ma=None, shi_yong="No"):
        self.__ma = JiHuoMa.random_ma(self)
        self.__zhuang_tai = shi_yong
        return "add is ok"

    @property
    def ma(self):
        return self.__ma
    # 获取某个激活码实例

    def get_zt(self):
        return self.__zhuang_tai

    def set_zt(self, value):
        if value == "yes" or "no":
            self.__zhuang_tai = value
        else:
            raise ValueError("plz input yes or no!")    

    zt = property(fget=get_zt, fset=set_zt, fdel=None, doc=None)
    # 获取和设置激活码是否被使用的状态

    def random_ma1(self):
        # 随即其中一组激活码
        assi = ("a", "b", "c", "d", "e", "f", "g",\
                "h", "i", "j", "k", "l", "m", "n",\
                "o", "p", "q", "r", "s", "t", "u",\
                "v", "w", "x", "y", "z", "1", "2",\
                "3", "4", "5", "6", "7", "8", "9"\
                )
        ma_1 = [x+y+z+c for x in random.choice(assi) for y in random.choice(assi)\
                for z in random.choice(assi) for c in random.choice(assi)]
        
        return ma_1

    def random_ma(self):
        return JiHuoMa.random_ma1(self) + "-" + JiHuoMa.random_ma1(self) + "-" + \
               JiHuoMa.random_ma1(self) + "-" + JiHuoMa.random_ma1(self)

j1 = JiHuoMa()

print(j1.ma())
print(j1.zt())

