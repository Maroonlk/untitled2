import time

class Person(object):
    def __init__(self):
        self._xue_liang = 100
        self._fang_yu = 0
        self._gong_ji = 5

    def shou_shang(self, value, who):
        if isinstance(value, int):
            self._xue_liang -= (value - self._fang_yu)
            print("你受到了来自{1}的{0}点伤害！".format(value, who))
            print("剩余{0}点血量！".format(self._xue_liang))
        else:
            raise ValueError("伤害类型错误")

    def gong_ji(self, who):



class Gamer(Person):
