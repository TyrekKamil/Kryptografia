def toBinary(a):
    if isinstance(a, str):
        a = int(a)
    x = int(bin(a)[2:])
    return makeBinary(x)


def makeBinary(x):
    return [int(d) for d in str(x)]

def binaryToDec(x):
    result = 0
    for i in range(len(x)-1, -1, -1):
        result = result + x[i] * pow(2, i)
    return result