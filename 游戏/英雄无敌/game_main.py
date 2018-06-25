'''
Hero's world! bate 0.1
Maroonlk
2018-06-25
'''
import time


# 设置地图
class GameMap(object):
    def __init__(self, size=[4, 5]):
        self.size = size
        self.map = [[x, y] for x in range(0, size[0]) for y in range(0, size[1])]


    # 打印地图
    def pri_Map(self, wei_zhi=None):
        for x, y in self.map:
            if wei_zhi == [x, y]:
                print("Y", end='')
            else:
                print("-", end='')
            if y == self.size[1] - 1:
                print("")





# map1.pri_Map([1, 1])
# print("=" * 20)
# map1.pri_Map([2, 2])


# 设置玩家类
class User(object):
    def __init__(self, name='Player01', gong_ji=5, xue_liang=100, fang_yu=0, wei_zhi=[0, 0]):
        self.name = name
        self._gong_ji_li = gong_ji
        self._xue_liang = xue_liang
        self._fang_yu = fang_yu
        self._wei_zhi = wei_zhi

    # 受伤害
    def shou_Shang(self, who, value):
        self._xue_liang -= (value - self._fang_yu / 2)

        if self._xue_liang > 0:
            print(" |{0}| 受到了 |{1}| 的 ~{2}~ 点伤害".format(self.name, who, value))
            print(" |{0}| 剩余HP: ~{1}~".format(self.name, self._xue_liang))
        else:
            print("GameOver!")
            return -1

    # 移动并且限制玩家无法在地图边缘移动溢出
    def move_User(self, fang_xiang):
        if fang_xiang == 'a' and self._wei_zhi[1] != 0:
            self._wei_zhi[1] -= 1
        if fang_xiang == 'd' and self._wei_zhi[0] != GameMap.size[0]:
            self._wei_zhi[1] += 1
        if fang_xiang == 'w' and self._wei_zhi[0] != 0:
            self._wei_zhi[0] -= 1
        if fang_xiang == 's' and self._wei_zhi[0] != GameMap.size[1]:
            self._wei_zhi[0] += 1


if __name__ == '__main__':
    print("欢迎来到《英雄无敌》的世界！")

    print("开始游戏... ... 载入中... ...")
    time.sleep(0.5)
    print("请输入你的角色名（可以为空）\r\n")
    name = input("角色名：")

    if name == '':
        p1 = User()
    else:
        p1 = User(name)

    print("\r\n游戏开始！你的角色名为：{0}\r\n".format(p1.name))
    print("你所在的地图将会是是这样的：")
    map1 = GameMap([4, 5])
    map1.pri_Map(p1._wei_zhi)
    print("你可以输入adsw来移动你的角色")

    while True:
        keyworld = input("移动：")
        p1.move_User(keyworld)
        map1.pri_Map(p1._wei_zhi)