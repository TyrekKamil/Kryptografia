from random import randint
from utils import generateElipcticCurve, znajdzLosowyPkt, dodajPktNaKrzywej, multiple_point
from math import sqrt


def losujP():
    p = randint(0, 10000000)
    if p % 4 != 3:
        return losujP()
    else:
        return p


def GenerujKlucze(): #P K BITÓW!!!!!TODO
    A, B, p = generateElipcticCurve(losujP())
    xp, yp = znajdzLosowyPkt(A, B, p)
    tmpMaxX = int(p + 1 - 2 * sqrt(p))
    x = randint(1, tmpMaxX)
    xq, yq = multiple_point(xp, yp, x, A, B, p)
    print("K_A = [\n\tE = [\n\t\t A =", A, "\n\t\t B =", B, "\n\t\t]\n\tp =", p, "\n\tP = (\n\t\tx =", xp,
          "\n\t\ty =", yp, "\n\t\t)\n\tQ = (\n\t\tx =", xq,
          "\n\t\ty =", yq, "\n\t\t)\n\t]")
    print("k_A = [\n\tE = [\n\t\t A =", A, "\n\t\t B =", B, "\n\t\t]\n\tp =", p, "\n\tP = (\n\t\tx =", xp,
          "\n\t\ty =", yp, "\n\t\t)\n\tQ = (\n\t\tx =", xq,
          "\n\t\ty =", yq, "\n\t\t)\n\tx =", x, "\n\t]")
    return 0


print(GenerujKlucze())
