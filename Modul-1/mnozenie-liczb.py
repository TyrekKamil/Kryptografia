def main():
    print(multiply([1, 0, 0], [1, 0, 0]))  # 2 * 4 = 8 [ 1 0 0 0 ]


def multiply(a, b):
    B = 2
    a = a[::-1]
    b = b[::-1]
    if b > a:
        a, b = swap(a, b)
    d = [0] * (len(a) + len(b) - 1)
    for i in range(0, len(a)):
        c = 0
        for j in range(0, len(b)):
            tmp = a[i] * b[j] + d[i] + c
            c, d[i+j] = Q(tmp, B)
    if c != 0:
        d.append(c)
    d = d[::-1]
    return d


def Q(x, y):
    return x//y, (x % y)


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


main()
