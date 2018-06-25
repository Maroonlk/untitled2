'''
Hero's world! bate 0.1
Maroonlk
2018-06-25
'''


class Person(object):
    def __init__(self, name='NoName', gong_ji=5, xue_liang=100, fang_yu=0):
        self.name = name
        self._gong_ji_li = gong_ji
        self._xue_liang = xue_liang
        self._fang_yu = fang_yu

    def gong_Ji(self, who, value=who._gong_ji_li):
        self._xue_liang -= (value - self._fang_yu / 2)

        print('{0}受到了来自{1}的{2}点伤害！'.format(self.name, who, value)
        print('{0}剩余HP:  {1}'.format(self.name, self._xue_liang)

    def go_move(self):
