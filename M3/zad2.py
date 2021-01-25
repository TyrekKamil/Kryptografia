from random import randint
from utils import generateElipcticCurve, znajdzLosowyPkt, dodajPktNaKrzywej, multiple_point
from math import sqrt


def losujBit(bits):
    s, i = 0, 0
    m = 1
    for i in range(0, bits):
        s = s + randint(0, 1) * m 
        m = m * 2
        i = i + 1
    return s

def losujP(bits):
    p = losujBit(bits)
    if p % 4 != 3:
        return losujP(bits)
    else:
        return p


def GenerujKlucze():  # TODO czasami nie ma odwrotnosci
    bits = 10
    A, B, p = generateElipcticCurve(losujP(bits))  # generowanie krzywej
    xp, yp = znajdzLosowyPkt(A, B, p)
    tmpMaxX = int(p + 1 - 2 * sqrt(p))  # maksymalna wartość X
    x = randint(1, tmpMaxX)
    xq, yq = multiple_point(xp, yp, x, A, B, p)
    return A, B, xp, yp, xq, yq, x


print(GenerujKlucze())
