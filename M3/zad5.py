
from zad1 import wielokrotnoscPkt
from utils import dodajPktNaKrzywej, generujPrzeciwny
from zad3 import decode

kappa_default = 100

def deszyfruj(A, B, p, xc1, yc1, xc2, yc2,  x, kappa=kappa_default): #TODO jaki x?
    xxc1, yxc1 = wielokrotnoscPkt(xc1, yc1, x, A, B, p) # xC1
    xxc1, yxc1 = generujPrzeciwny(xxc1, yxc1, p) # - xC1
    Pm = dodajPktNaKrzywej(A, B, p, xc2, yc2, xxc1, yxc1) # Pm = C2 - xC1
    M = decode(Pm, kappa)
    return M

print(deszyfruj(38479412483,434747390852,638061376279,629637834291,131275199216,442536171476,21188241970,1515532508))