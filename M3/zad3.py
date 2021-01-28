from random import randint
from utils import isModSqr, znajdzB
from math import sqrt 

kappa_default = 100


def decode(xpm, kappa):
    return (xpm) // kappa


def encode(A, B, p, M, kappa=kappa_default):  # TODO y, x czasami blisskie
    if M <= p/kappa:
        for j in range(0, kappa):
            x = (M * kappa + j) % p
            f =- (pow(x, 3, p) + A * (x) + B) % p
            if isModSqr(f, p):
                y1, y2 = znajdzB(f, p)
                if y1 > 0:
                    return x, y1, decode(x, kappa) == M
                else:
                    return x, y2, decode(x, kappa) == M
    return None, None


def Zad3(A, B, p, M, kappa=kappa_default):
    result = encode(A, B, p, M)
    while result[0] is None or result[1] is None:
        result = encode(A, B, p, M)
    return A, B, p, kappa, M, result


print(Zad3(165322775454904,124574101102043,233782525984873,1453869503676))
