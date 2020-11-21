from odejmowanie import substract
from mnozenieLiczb import multiply
from dzielenieReszta import div
from dodawanieLiczb import add

def ExtendedGCD(a, b):
    old_r, r = a, b
    old_s, s = [1], [0]
    old_t, t = [0], [1]

    while r != [0]:
        q = div(old_r, r)[0]
        old_r, r = r, substract(old_r, multiply(q, r))
        old_s, s = r, substract(old_s, multiply(q, s))
        old_t, t = r, substract(old_t, multiply(q, t))
    return r, s, t



a = [1, 0, 1, 1, 1]
b = [1, 0, 1, 1, 1, 1]

print(ExtendedGCD(a, b))


