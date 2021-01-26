from utils import dodajPktNaKrzywej, generujPrzeciwny

def wielokrotnoscPkt(A, B, p, x, y, n): #TODO ujemne

    xq = x
    yq = y
    xr, yr = None, None
    
    while n > 0:
        if n % 2 == 1:
            xr, yr = dodajPktNaKrzywej(A, B, p, xr, yr, xq, yq)
            n = n - 1 # pomnożenie przez znak - aby wiedział, w którą stronę iść (dod/uj)
        xq, yq = dodajPktNaKrzywej(A, B, p, xq, yq, xq, yq)
        n = n // 2
    return xr, yr
