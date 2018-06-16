try:
    num = int(input("请输入一个数字： "))
    num2 = 100 / num
    print("计算结果是 {0}".format(num2))


except ZeroDivisionError as e:
    print(e)
    print(e.__str__())

except Exception as e:
    print("hhh")
    print(e)

