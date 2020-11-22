

def multiply(a, b):
    B = 2
    a = a[::-1]
    b = b[::-1]
    if len(b) > len(a):
        a, b = swap(a, b)
    d = [0] * (len(a) + len(b))
    for i in range(0, len(a)):
        c = 0
        for j in range(0, len(b)):
            tmp = a[i] * b[j] + d[i+j] + c
            c, d[i+j] = Q(tmp, B)
        d[i+len(b)] = c
    return optimize(d)


def Q(x, y):
    return x//y, (x % y)


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

def optimize(x):
    index = 0
    x = x[::-1]
    for i in range(0, len(x) - 1):
        if(x[i] == 0):
            index = index + 1 
        else: 
            break
    x = x[index:]
    return x