from dzielenieReszta import div


def NWD(a, b):
    if a == [0]:
        return b
    return NWD(div(b, a)[1], a)


def NWDmod(a, b):
    while b != [1]:
        q, r = div(a, b)
        print(a, " = ", q, "(", b, ") + ", r)
        b = a
        a = r
    return q


a, b = [1, 0, 1], [1, 0]  # 5 mod 2
print(NWDmod(a, b))
