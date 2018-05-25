def count():
    fs = []
    flag = 0
    for i in range(1, 4):
        flag += 1
        print("1  x = {0}\tfs have:{1}\tflag = {2}".format(i, len(fs), flag))

        def f(j):
            print("2  x = {0}\tfs have:{1}\tflag = {2}".format(i, len(fs), flag))
            return j * j

        fs.append(f(i))
        print(len(fs))
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)


# *****************************************************************************************
def count2():
    fs = []
    flag = 0
    for i in range(1, 4):
        flag += 1
        print("1  x = {0}\tfs have:{1}\tflag = {2}".format(i, len(fs), flag))

        def f(j):
            def g():
                return j * j

            print("2  x = {0}\tfs have:{1}\tflag = {2}".format(i, len(fs), flag))
            return g

        fs.append(f(i))
    return fs


n1, n2, n3 = count2()
print(n1(), n2(), n3())
