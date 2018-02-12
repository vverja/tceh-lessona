import time


def duration_of_runtime(func):
    def inner(*args):
        p1 = time.time()
        s = func(*args)
        p2 = time.time()
        dur = p2 - p1
        print('Duration of function execution ', dur)
        return s
    return inner


@duration_of_runtime
def sum1(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum


@duration_of_runtime
def sum2(l):
    return sum(l)


def main():
    ll = [23,444,2321,4545,90909,93043,33,289,802,656,987,4232,4235,888,11,4432]
    print(sum1(ll))
    print(sum2(ll))

if __name__ == '__main__':
    main()