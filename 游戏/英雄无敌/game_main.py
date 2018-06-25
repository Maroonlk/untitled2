'''
Hero's world! bate 0.1
Maroonlk
2018-06-25
'''

class GameMap(object):
    def __init__(self, size=[4, 4]):
        self.size = size
        self.map = [[x,y] for x in range(0,size[0]) for y in range(0,size[1])]

    def pri_Map(self):
        for x,y in self.map:
            print("#", end='')
            if y == self.size[1]-1:
                print("")


map1 = GameMap()
map1.pri_Map()



class User(object):
    def __init__(self, name='Player01', gong_ji=5, xue_liang=100, fang_yu=0, wei_zhi=[0,0]):
        self.name = name
        self._gong_ji_li = gong_ji
        self._xue_liang = xue_liang
        self._fang_yu = fang_yu
        self._wei_zhi = wei_zhi

    def shou_Shang(self, who, value):
        self._xue_liang -= (value - self._fang_yu / 2)

        if self._xue_liang > 0:
            print(" |{0}| 受到了 |{1}| 的 ~{2}~ 点伤害".format(self.name, who, value))
            print(" |{0}| 剩余HP: ~{1}~".format(self.name, self._xue_liang))
        else:
            print("GameOver!")
            return -1

    def move_User(self, fang_xiang):
        if fang_xiang == 'a' and self._wei_zhi[0] != 0:
            self._wei_zhi[0] -= 1
        if fang_xiang == 'd' and self._wei_zhi[0] != GameMap.size[1]:
            self._wei_zhi[0] += 1
