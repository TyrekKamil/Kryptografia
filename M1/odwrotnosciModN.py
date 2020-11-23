from odejmowanie import odejmij
from mnozenieLiczb import multiply
from dzielenieReszta import div
from dodawanieLiczb import add

def egcd(a, b):
    if a == [0]:
        return (b, [0], [1])
    else:
        g, y, x = egcd(div(b,a)[1], a)
        z = odejmij(x, multiply(div(b,a)[0],y)) 
        #x - (b // a) * y
        return (g, z, y)
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != [1]:
        raise Exception('modular inverse does not exist')
    else:
        return div(x, m)[1]


a = [1, 0, 1, 1, 1]
b = [1, 0, 1, 1, 1, 1]

print(egcd(a, b))


