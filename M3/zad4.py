
from random import randint
from utils import dodajPktNaKrzywej
from zad1 import wielokrotnoscPkt
from math import sqrt


def szyfrujElgamal(A, B, p, xp, yp, xq, yq, M): #TODO czasmai nie ma odwrotnosci, wyniki
    xpm = ypm = M
    y = randint(1, int(p + 1 - 2 * sqrt(p)))
    xc1, yc1 = wielokrotnoscPkt(A, B, p, xp, yp, y)
    xyq, yyq = wielokrotnoscPkt(A, B, p, xq, yq, y)
    xc2, yc2 = dodajPktNaKrzywej(xpm, ypm, xyq, yyq, A, B, p)
    return A, B, p, xq, yq, xp, yp, M, xc1, yc1, xc2, yc2

print(szyfrujElgamal(615310606977377600,368641938789887509,630858080829889823,30971916540155906,256563467271589783,48364257713943279,607273520761100679,6152992012277699))