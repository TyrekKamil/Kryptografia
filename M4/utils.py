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
    result = []
    for i in range(0, 8):
        result.append(randint(0, 1))
    return result

def RandomHex():
    digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    a = choice(digit)
    b = choice(digit)
    return a+b
