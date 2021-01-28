from random import randint
from utils import generateElipcticCurve, znajdzLosowyPkt, dodajPktNaKrzywej
from zad1 import wielokrotnoscPkt
from math import sqrt, log


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


def GenerujKlucze(k):
    bits = 10
    A, B, p = generateElipcticCurve(losujP(bits))  # generowanie krzywej
    xq, yq = znajdzLosowyPkt(A, B, p) # Q
    tmpMaxX = int(p + 1 - 2 * sqrt(p))  # maksymalna wartość X
    if log(tmpMaxX, 2) > k/4: # zalozenie - rzad > k/4
        x = randint(1, tmpMaxX)
        xp, yp = wielokrotnoscPkt(A, B, p, xq, yq, x) # P = x * q
        return A, B, p, xq, yq, xp, yp, x
    return None


#print(GenerujKlucze(8))
