from utils import dodajPktNaKrzywej

def wielokrotnoscPkt(A, B, p, x, y, n): #TODO ujemne
    xq = x
    yq = y
    xr, yr = None, None

    if n >= 0:
        sign = 1
    else:
        sign = -1 # znak n - do warunku while, aby wiedział, w którą strone iść
        
    while (n > 0 and sign == 1) or (n < 0 and sign == -1):
        if n % 2 == 1:
            xr, yr = dodajPktNaKrzywej(A, B, p, xr, yr, xq, yq)
            n = n - ( 1 * sign) # pomnożenie przez znak - aby wiedział, w którą stronę iść (dod/uj)
        xq, yq = dodajPktNaKrzywej(A, B, p, xq, yq, xq, yq)
        n = n // 2
    return xr, yr

print(wielokrotnoscPkt(138, 68, 157, 25, 60, -130))