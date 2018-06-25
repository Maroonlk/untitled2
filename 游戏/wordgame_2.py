print('----------------我爱鱼c工作室------------------')
import random
import time

flag = 0
guess = int(random.uniform(0, 1000111))


while True:
    flag += 1
    temp = int(random.uniform(0, 1000111))

    if temp == guess:
        print("猜对了，用了{0}次！".format(flag))
        break
    elif temp < guess:
        print(temp)
    elif temp > guess:
        print(temp)

print("Game over!")
print(guess)