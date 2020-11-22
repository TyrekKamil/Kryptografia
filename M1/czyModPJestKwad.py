from szybkiePotegowanie import exp
from odejmowanie import odejmij
from dzielenieReszta import div


def isModSqr(p, m):
    if exp(m, (div(odejmij(p, [1]), [1, 0])[0]), p) == [1]:
        return 'Tak'
    else:
        return 'Nie'
