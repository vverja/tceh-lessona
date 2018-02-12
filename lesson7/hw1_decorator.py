def function_is_canceled(func):
    def inner(x, y):
        print("Function ", func.__name__, " is canceled")
    return inner


@function_is_canceled
def mult(x, y):
    return x*y


def main():
    print(mult(5, 56))


if __name__ == '__main__':
    main()

