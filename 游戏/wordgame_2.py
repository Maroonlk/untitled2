print('----------------我爱鱼c工作室------------------')
import random
import time

flag = 0
guess = int(random.uniform(0, 1000))


while True:
    flag += 1
    temp = int(random.uniform(0, 1000))

    if temp == guess:
        print("猜对了，用了{0}次！".format(flag))
        break
    elif temp < guess:
        print("小了哟~大一点... ...")
    elif temp > guess:
        print("太大了嘛... ... 小一点")

print("Game over!")
print(guess)
