from random import randint
from utils import isModSqr, znajdzB

kappa_default=100

def decode(xpm, kappa):
    return (xpm) // kappa

def encode(A, B, p, M, kappa=kappa_default): #TODO y, x czasami blisskie
    N = randint(1, int(0.05 * p)) + M

    if N * kappa < p:
        for j in range(1, kappa + 1):
            x = (M * kappa + j) % p
            f = (pow(x, 3, p) + A * x + B) % p
            if isModSqr(f, p):
                y1, y2 = znajdzB(f, p)
                if y1 > 0:
                    return x, y1, decode(x, kappa) == M
                else:
                    return x, y2, decode(x, kappa) == M
    return None, None

result = encode(550887326258000 ,761654032839972 ,1008614860794511 ,8092922464793 )
while result[0] is None or result[1] is None:
    result = encode(550887326258000 ,761654032839972 ,1008614860794511 ,8092922464793 )

print(result)