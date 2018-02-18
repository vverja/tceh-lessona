from random import randint


def gen(length):
    for i in range(length):
        yield randint(0, 100)


def zrange(begin, end=0, step=1):
    if begin <= 0:
        raise ValueError
    if begin > end and end !=0:
        while begin > end:
            yield begin
            begin = begin - step
    elif end == 0:
        end = begin
        begin = 0
    while begin < end:
        yield begin
        begin = begin + step

def zmap(func, z_list):
    pass

def zenum(z_list):
    pass

def zzip(func, z_list):
    pass

gen = [s for s in gen(5)]

print(gen)


s = list(zrange(10))
print(s)
