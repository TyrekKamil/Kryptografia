
from zad1 import wielokrotnoscPkt
from utils import dodajPktNaKrzywej, generujPrzeciwny, random_prime, znajdzLosowyPkt
from zad3 import decode
from zad2 import GenerujKlucze
from random import randint
from math import sqrt

kappa_default = 100


def deszyfruj(A, B, p, xc1, yc1, xc2, yc2, x, kappa=kappa_default):  # TODO jaki x?
    xxc1, yxc1 = wielokrotnoscPkt(xc1, yc1, p, A, B, x)  # xC1
    xxc1, yxc1 = generujPrzeciwny(xxc1, yxc1, p)  # - xC1
    Pm = dodajPktNaKrzywej(A, B, p, xc2, yc2, xxc1, yxc1)  # Pm = C2 - xC1
    M = decode(Pm[0], kappa)
    return M


def Zad5():
    maxBits = 10
    p = random_prime(maxBits)
    while p % 4 != 3:
        p = random_prime(maxBits)
    A = randint(0, p-1)
    B = randint(0, p-1)
    xq, yq = znajdzLosowyPkt(A, B, p)

    k = randint(1, int(p + 1 - 2 * sqrt(p)))
    x = randint(1, int(p + 1 - 2 * sqrt(p)))

    M = randint(0, p//kappa_default-1)
    
    xp, yp = wielokrotnoscPkt(xq, yq, p, A, B, x) # P = x * Q
    xpm, ypm =  znajdzLosowyPkt(A, B, p)

    xc1, yc1 = wielokrotnoscPkt(xq, yq, p, A, B, k) # C1 = k * Q
    xc2, yc2 = wielokrotnoscPkt(xp, yp, p, A, B, k) # k*P
    xc2, yc2 = dodajPktNaKrzywej(A, B, p, xp, yp, xpm, ypm) # C2  = k*P + PM

    print(A, B, p, xc1, yc1, xc2, yc2, deszyfruj(A, B, p, xc1, yc1, xc2, yc2, x))

Zad5()