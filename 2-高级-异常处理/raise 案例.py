if __name__ == '__main__':
    try:
        print("I love you")
        print(3.1415926)
        # 手动引发
        raise ValueError
        print("我还没完")

    except NameError as e:
        print(e)

    except ValueError as e:
        print("ValueError")

    except Exception as e:
        print(e)
    finally:
        print("I never index")

