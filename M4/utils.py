from random import randint, choice

def HexToDec(n):
    return int(n, 16)

def DecToHex(n):
    return hex(int(n))[2:]

def HexToBin(n):
    dec = HexToDec(n)
    return DecToBin(dec)[2:]

def DecToBin(n):
    return [x for x in bin(int(n))]

def BinToDec(n):
    return str(int(n, 2))

def BinToHex(n):
    n = ",".join(n).replace(",", "")
    return DecToHex(BinToDec(n))

def losujF():
    result = [1]
    for i in range(0, 8):
        result.append(randint(0, 1))
    if fermat_test("".join(str(x) for x in result)) is False:
        losujF()
    return result


def fermat_test(n):
    n = int(n)
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(1000):
        a = randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def RandomHex():
    digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    a = choice(digit)
    b = choice(digit)
    return a+b
