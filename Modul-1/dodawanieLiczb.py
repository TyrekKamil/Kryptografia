import string


def main():
    print(add([1, 0], [1, 0, 0]))


def add(a, b):
    if b > a:
        [a,b] = swap(a, b)
    a = a[::-1]
    b = b[::-1]
    c = 0
    d = [None] * len(a)
    for i in range(len(b)):
        tmp = a[i] + b[i] + c
        [c, d[i]] = Q(tmp, 2)

    for i in range(len(b), len(a)):
        tmp = a[i] + c
        [c, d[i]] = Q(tmp, 2)

    if c != 0:
        d.append(c)

    d = d[::-1]
    return d


def Q(x, y):
    return [x//y, (x % y)]

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return [a, b]

main()
