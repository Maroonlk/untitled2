# 测量程序运行时间间隔实验
import time
import timeit


def p():
    time.sleep(3.6)

# t1 = time.time()
# p()
# print(time.time() - t1)


c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

# 利用timeit 调用代码，执行100000次， 查看运行时间
# t = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)

# 测量代码c执行100000次运行结果

# t2 = timeit.timeit(stmt=c, number=100000)

# print(t1)
# print(t2)

# timeit  可以执行一个函数，来测量一个函数的执行时间

def doIT():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))

# 执行函数，重复10次
t = timeit.timeit(stmt=doIT, number=10)
print(t)

s = '''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
'''
# 执行doIt(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创造了一个小环境
# 在创作的小环境中，代码执行的顺序是
    '''
    def doIt(num):
        pass
    num = 3
    doIt(num)
    '''
t = timeit.timeit(stmt="doIt(num)", setup=s+"num=3", number=10)
print(t)