
def fdecor(func):
    count = [0]
    def wrapper():
        r = func()
        print('Function ', func.__name__, ' executed ', count[0], ' times')
        return r

    count[0] += 1
    return wrapper

@fdecor
def mult():
    return 100

mult()
mult()
mult()
