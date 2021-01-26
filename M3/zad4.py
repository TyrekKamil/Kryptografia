
from random import randint
from utils import dodajPktNaKrzywej
from zad1 import wielokrotnoscPkt
from math import sqrt


def szyfrujElgamal(A, B, p, xq, yq, xp, yp, M):
    xpm = ypm = M
    k = randint(1, int(p + 1 - 2 * sqrt(p)))
    xc1, yc1 = wielokrotnoscPkt(A, B, p, xq, yq, k) # C1 = k * q
    kpx, kpy = wielokrotnoscPkt(A, B, p, xp, yp, k) # k * P
    xc2, yc2 = dodajPktNaKrzywej(A, B, p, xpm, ypm, kpx, kpy) # C2 = Pm + kP
    return xc1, yc1, xc2, yc2

def Zad4(A, B, p, xp, yp, xq, yq, M):
    return A, B, p,  xp, yp, xq, yq, M, szyfrujElgamal(A, B, p, xp, yp, xq, yq, M)

print(Zad4(615310606977377600,368641938789887509,630858080829889823,30971916540155906,256563467271589783,48364257713943279,607273520761100679,6152992012277699))