def substract(a, b):
    d = 0
    a = a[::-1]
    b = b[::-1]
    l = len(b)
    k = len(a)
    c = [0] * k
    for i in range(0, l):
        tmp = a[i] - b[i] + d
        d, c[i] = tmp//2, tmp % 2
    for i in range(l, k):
        tmp = a[i] - d
        d, c[i] = tmp//2, tmp % 2
    return optimize(c)


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


def odejmij(a, b):
    a = a[::-1]
    b = b[::-1]
    l = len(b)
    k = len(a)
    c = [0] * k
    for i in range(0, l):
        if (a[i] == 0 and b[i] == 0) or (a[i] == 1 and b[i] == 1):
            c[i] = 0
           # print(i, "#1", c[i])
        elif a[i] == 1 and b[i] == 0:
            c[i] = 1
          #  print(i, "#2", c[i])
        elif a[i] == 0 and b[i] == 1:
            j = i + 1
            a[i] = 2
            while a[j] == 0:
                a[j] = 1
                j += 1
            a[j] = 0
            c[i] = a[i] - b[i]
           # print(i, "#3", c[i])
    for i in range(l, k):
        c[i] = a[i]
      #  print(i, "#4")
    return optimize(c)


a, b = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1], [
    1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
#print(odejmij(a, b))
