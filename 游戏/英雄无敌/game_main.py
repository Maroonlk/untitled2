'''
Hero's world! bate 0.1
Maroonlk
2018-06-25
'''
import time
import random


# 设置地图
class GameMap(object):
    map_size = None
    def __init__(self, size=[4, 5]):
        self.size = size
        self.map = [[x, y] for x in range(0, size[0]) for y in range(0, size[1])]
        GameMap.map_size = size

    # 打印地图
    def pri_Map(self, wei_zhi=None):
        for x, y in self.map:
            if wei_zhi == [x, y]:
                print("O", end='')
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
        self.ji_neng = {
            "1":self._gong_ji_li * random.choice(1,1,1,1.5)
        }
    # 受伤害



    # 移动并且限制玩家无法在地图边缘移动溢出
    def move_User(self, fang_xiang):
        if fang_xiang == 'a' and self._wei_zhi[1] != 0:
            self._wei_zhi[1] -= 1
        if fang_xiang == 'd' and self._wei_zhi[1] != GameMap.map_size[1]-1:
            self._wei_zhi[1] += 1
        if fang_xiang == 'w' and self._wei_zhi[0] != 0:
            self._wei_zhi[0] -= 1
        if fang_xiang == 's' and self._wei_zhi[0] != GameMap.map_size[0]-1:
            self._wei_zhi[0] += 1

#设置怪物类
class GuaiWu(object):
    def __init__(self, name, gong_ji, xue_liang, fang_yu, wei_zhi=None):
        self.name = name
        self.gong_ji = gong_ji
        self.xue_liang = xue_liang
        self.fang_yu = fang_yu
        self.wei_zhi = wei_zhi
        self.ji_neng = {
            '1':self.gong_ji * random.choice(1,1,1,1.5)
        }

    def shou_Shang(self, who, value):
        self.xue_liang -= (value - self.fang_yu/2)

        if self.xue_liang > 0:


slm = GuaiWu("史莱姆", gong_ji=3, xue_liang=10, fang_yu=1)




if __name__ == '__main__':
    print("欢迎来到《英雄无敌》的世界！")

    print("开始游戏... ... 载入中... ...")
    time.sleep(0.5)
    print("请输入你的角色名（可以为空）\r\n")
    name = input("角色名：")

    if name == '':    #检测是否空ID
        p1 = User()
    else:
        p1 = User(name)

    print("\r\n游戏开始！你的角色名为：{0}\r\n".format(p1.name))
    print("你所在的地图将会是是这样的：")
    map1 = GameMap([4, 5])
    map1.pri_Map(p1._wei_zhi)
    print("当你走到右下角时，你就胜利了！\r\n")
    print("你可以输入adsw来移动你的角色")

    #随机怪物刷新的坐标
    guai_wu_list = random.sample(map1.map, random.choice(range(0, GameMap.map_size[0] * GameMap.map_size[1])))

    def gong_ji(fa_dong, bei_dong, shang_hai):
        print(" |{0}| 发动了攻击，对 |{1}| 造成了 |{2}| 点伤害！".format(fa_dong, bei_dong, shang_hai))
        p1._xue_liang -= fa_dong.gong_ji - bei_dong._fang_yu / 2

        print(" |{0}| 剩余血量： |{1}| ".format(bei_dong, bei_dong._xue_liang))

    while True:
        keyworld = input("移动：")
        p1.move_User(keyworld)
        map1.pri_Map(p1._wei_zhi)


        if p1._wei_zhi != [0, 0]:
            if p1._wei_zhi in guai_wu_list:
                print("##遭遇{0}！   准备战斗！".format(slm.name))
                while True:
                    a = input("攻击：请输入|1|使用普通攻击:")

                    if a == '1':
                        print("{0}发动了攻击！")




        if p1._wei_zhi == [GameMap.map_size[0]-1, GameMap.map_size[1]-1]:
            print("~~~~~~你赢了！！~~~~~")
            break