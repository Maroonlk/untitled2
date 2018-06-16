if __name__ == '__main__':
    try:
        num = int(input("input your num: "))
        rst = 100 / num
        print("计算结果是 {0}".format(rst))
    except Exception as e:
        print(e)
        print(type(e))

    else:
        print("No Exception")

    finally:
        print("I am!")
