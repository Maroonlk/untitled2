print('----------------我爱鱼c工作室------------------')
import random

flag = 0
guess = int(random.uniform(0, 10))
do_one = ''

while flag < 3:
    temp = int(input("{0}输入一个数字，来猜一猜吧！:".format(do_one)))
    flag += 1
    do_one = '再'

    if temp == guess and flag == 1:
        print("哇！你居然一次就猜对了")
        break
    elif temp == guess:
        print("恭喜你，猜对了，你用了{0}次！".format(flag))
        break
    elif temp < guess:
        print("小了哟~大一点... ...")
    elif temp > guess:
        print("太大了嘛... ... 小一点")
    if flag > 2:
        print("三次机会用完咯！")
print("Game over!")
print(guess)


