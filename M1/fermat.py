from math import ceil, floor
import random

def optimize(factors):
    j = {}
    result = ""
    for i in range(0, len(factors)):
        j[str(factors[i])] = factors.count(factors[i])
    for i in j:
        if j[i] == 1:
            result = result + str(i) + " * "
        else:
            result = result + str(i) + "^" + str(j[i]) + " * "
    return result[:len(result)-2]


def fermat(p, result):
    x = int(ceil(p ** 0.5))
    while True:
        z = x * x - p
        y = int(floor(z ** 0.5))
        if z == y * y:
            m = x + y
            n = x - y
            if n == 1:
                break
            fermat(m, result)
            fermat(n, result)
            return
        x += 1
    result.append(p)

def fermatTest(a, n):
    result = []
    while n % 2 == 0:
        n = n // 2
        result.append(2)
    if n > 1:
        fermat(n, result)

    if len(result) == 1:
        return "Nie", result[0]
    else:
        sorted_Factors = list(map(str, sorted(result)))
        return "Tak", optimize(sorted_Factors)