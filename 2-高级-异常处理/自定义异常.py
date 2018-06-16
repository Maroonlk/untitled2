if __name__ == '__main__':

    class DanaError(ValueError):
        def __str__(self):
            return "DanaError"

    try:
        print("I love you")
        print(3.1415926)
        # 手动引发
        raise DanaError
        print("我还没完")

    except NameError as e:
        print(e)

    except DanaError as e:
        print(e)

    except ValueError as e:
        print("ValueError")

    except Exception as e:
        print(e)
    finally:
        print("I never index")