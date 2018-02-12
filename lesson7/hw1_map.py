l = [1, 4, 5, 30, 99]

ll = list(map(lambda x: x % 5, l))

print(ll)

p = [3, 4, 90, -2]

pp = list(map(lambda x: str(x), p))

print(pp)

k = ['some', 1, 'v', 40, '3a', str]

kk = list(filter(lambda x: not isinstance(x, str), k))

print(kk)

from functools import reduce

t = ['some', 'other', 'value']
def sum_len(x, y):
    if isinstance(x, str):
        return len(x)+ len(y)
    else:
        return x + len(y)

tt = reduce(sum_len, t)
print(tt)
