from utils import dodajPktNaKrzywej, generujPrzeciwny

def wielokrotnoscPkt(A, B, p, x, y, n):

    xq = x
    yq = y
    xr, yr = None, None

    sign = 1
    if n < 0: # sprawdzenie znaku
        sign = -1
        n = n * -1 # jezeli jest ujemne to sign = -1, z n "usuwamy minusa"
 
    while n > 0:
        if n % 2 == 1:
            xr, yr = dodajPktNaKrzywej(A, B, p, xr, yr, xq, yq)
            n = n - 1 # pomnożenie przez znak - aby wiedział, w którą stronę iść (dod/uj)
        xq, yq = dodajPktNaKrzywej(A, B, p, xq, yq, xq, yq)
        n = n // 2
    if sign == -1:
        xr, yr = generujPrzeciwny(p, xr, yr) # Traktujemy cały czas jak dodanie, dopiero na końcu mnożymy przez minusa, który jest przy "n" - czyli generujemy element przeciwny
    return xr, yr

def Zad1(A, B, p, x, y, n):
    return A, B, p, x, y, wielokrotnoscPkt(A, B, p, x, y, n), n

#print(Zad1(138,68,157,25,60,-130))