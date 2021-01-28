from random import randint
from utils import isModSqr, znajdzB, random_prime
from math import sqrt

kappa_default = 100


def decode(xpm, kappa):
    return (xpm) // kappa  # x/k


def encode(A, B, p, M, kappa=kappa_default):
    if M <= p/kappa:
        for j in range(0, kappa):
            x = (M * kappa + j) % p  # k*M+j - Koblitz
            f = - (pow(x, 3, p) + A * (x) + B) % p
            if isModSqr(f, p):
                y1, y2 = znajdzB(f, p)
                if y1 > 0:
                    return x, y1, decode(x, kappa) == M
                else:
                    return x, y2, decode(x, kappa) == M
    return None, None


def Zad3(kappa=kappa_default):
    maxBits = 10
    p = random_prime(maxBits)
    while p % 4 != 3:
        p = random_prime(maxBits)
    A = randint(0, p-1)
    B = randint(0, p-1)
    M = randint(0, p//kappa_default-1)
    result = encode(A, B, p, M)
    while result[0] is None or result[1] is None:
        result = encode(A, B, p, M)
    return A, B, p, kappa, M, result


#print(Zad3())
