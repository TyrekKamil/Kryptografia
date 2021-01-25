from random import randint

def generateElipcticCurve(p):
    result = False # flaga, której końcowa wartość definuje, czy z danych wartości stworzymy krzywą eliptyczną
    while result == False: # dopóki jest false...
        A = randint(0, p - 1 )
        B = randint(0, p - 1) # losowe A B
        delta = (4 * pow(A, 3, p) + 27 * pow(B, 2, p)) % p # warunek 4A3 + 27B2 = 0 (mod p)
        if delta != 0: # jeśli nie jest równe, para spełnia warunek - true
            result = True
    return A, B, p 


def znajdzLosowyPkt(A, B, p):
    x = randint(0, p)
    y = randint(0, p) # losowanie x i y z przedziału (0, p) - bez p 

    while not (czyNalezy(A, B, p, x, y)): # warunek punktu krzywej
        x = randint(0, p)
        y = randint(0, p)
    return x, y

def czyNalezy(A, B, p, x, y):
    result = False # kontrolka - domyslnie false, przy spełnionym warunki TRUE
    if ((y**2) % p) == ((pow(x, 3, p) + A*x + B) % p): # y2 = x3 + Ax + B oraz p jako modulo
        return True
    return result

def multiple_point(x, y, n, a, b, p):
    xq = x
    yq = y
    xr, yr = None, None
    while n > 0:
        if n % 2 == 1:
            xr, yr = dodajPktNaKrzywej(xr, yr, xq, yq, a, b, p)
            n -= 1
        xq, yq = dodajPktNaKrzywej(xq, yq, xq, yq, a, b, p)
        n = n // 2
    return xr, yr

def dodajPktNaKrzywej(A, B, p, x1, y1, x2, y2):
    # Przypadek P = -Q
    if (x1, y1) == (x2, ((-1*y2) % p)):
        return None, None
    elif x1 is None and y1 is None:
        return x2, y2
    elif x2 is None and y2 is None:
        return x1, y2
    # Przypadek P != Q
    elif (x1) != (x2):
        lam = ((y2 - y1) * (modinv(p, (x2-x1) % p))[1]) % p
        x3 = (pow(lam, 2, p) - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return x3, y3
    # Przypadek P = Q
    elif (x1, y1) == (x2, y2):
        lam = (((3 * pow(x1, 2)) + A) * (pow((2 * y1), -1, p))) % p
        x3 = (pow(lam, 2) - 2 * x1) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return x3, y3

def exp(b, k, n): #n b k -> b k n
    r = [1] 
    x = div(b, n)[1]
    
    for i in range(len(k) - 1, -1, -1):
        if k[i] == 1:
            r = multiply(r, x)
            r = div(r, n)[1]
        x  = multiply(x, x)
        x  = div(x, n)[1]
    return r

def toBinary(a):
    if isinstance(a, str):
        a = int(a)
    x = int(bin(a)[2:])
    return makeBinary(x)


def makeBinary(x):
    return [int(d) for d in str(x)]

def binaryToDec(x):
    result = 0
    for i in range(len(x)-1, -1, -1):
        result = result + x[i] * pow(2, i)
    return result

def multiply(a, b):
    B = 2
    a = a[::-1]
    b = b[::-1]
    if len(b) > len(a):
        a, b = swap(a, b)
    d = [0] * (len(a) + len(b))
    for i in range(0, len(a)):
        c = 0
        for j in range(0, len(b)):
            tmp = a[i] * b[j] + d[i+j] + c
            c, d[i+j] = Q(tmp, B)
        d[i+len(b)] = c
    return optimize(d)

def div(a, b):
    if len(b) > len(a):
        return 0, a
    a = a[::-1]
    b = b[::-1]

    B = 2
    k = len(a)
    l = len(b)
    r = [0] * (k+1)
    q = [0] * (k+1)

    for i in range(0, k):
        r[i] = a[i]

    for i in range(k - l, -1, -1):
        q[i] = (r[i + l] * B + r[i+l-1]) // (b[l-1])
        if q[i] >= B:
            q[i] = B - 1
        c = 0
        for j in range(0, l):
            tmp = r[i+j] - q[i] * b[j] + c
            c, r[i+j] = Q(tmp, B)
        r[i+l] = r[i+l] + c
        while r[i+l] < 0:
            c = 0
            for j in range(0, l):
                tmp = r[i+j] + b[j] + c
                c, r[i+j] = Q(tmp, B)
            r[i+l] = r[i+l] + c
            q[i] = q[i] - 1
    q = optimize(q)
    r = optimize(r)
    return(q, r)



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = egcd(b%a, a)
    
    tmp = x
    x = y - (b//a) * x
    y = tmp
    return (g, x, y)
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g == 1:
        if m == 1:
            return [1]
        return g, x%m
    else:
        return g, []

def Q(x, y):
    return x//y, (x % y)


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

def optimize(x):
    index = 0
    x = x[::-1]
    for i in range(0, len(x) - 1):
        if(x[i] == 0):
            index = index + 1 
        else: 
            break
    x = x[index:]
    return x