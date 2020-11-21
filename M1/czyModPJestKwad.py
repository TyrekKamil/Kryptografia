from szybkiePotegowanie import exp
from odejmowanie import odejmij
from dzielenieReszta import div


def isModSqr(b, p):
    if exp(b, (div(odejmij(p, [1]), [1, 0])[0]), p) == 1:
        return True
    else:
        return False


b, p = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
print("#1", div(odejmij(p, [1]), [1, 0])[0])
print("#2", odejmij(p, [1]))
print(isModSqr(b, p))
print(exp(b, (div(odejmij(p, [1]), [1, 0])[0]), p))
b,p=6977,3641
print(pow(b, ((p-1)//2), p))
