import time

def deco(func):
    def func_2():
        startT = time.time()
        func()
        endT = time.time()
        useT = (endT-startT) * 1000
        print(useT)
    return func_2

@deco
def myfunc():
    print("Myfunc start!")
    time.sleep(1.1)
    print("Mufunc end!")


myfunc()
