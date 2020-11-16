def toBinary(a):
    if isinstance(a, str):
        a = int(a)
    x = int(bin(a)[2:])
    return makeBinary(x)


def makeBinary(x):
    return [int(d) for d in str(x)]