from tobinary import binaryToDec, toBinary

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = egcd(b%a, a)
    
    tmp = x
    x = y - (b//a) * x
    y = tmp
    return (g, x, y)
 
def modinv(a, m):
    a = binaryToDec(a)
    m = binaryToDec(m)
    g, x, y = egcd(a, m)
    if g == 1:
        if m == 1:
            return [1]
        return toBinary(g), toBinary(x%m)
    else:
        return toBinary(g), []