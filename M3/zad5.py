
from zad1 import wielokrotnoscPkt
from utils import dodajPktNaKrzywej, generujPrzeciwny

def deszyfruj(A, B, p, xc1, yc1, xc2, yc2,  x):
    xxc1, yxc1 = wielokrotnoscPkt(xc1, yc1, x, A, B, p)
    xxc1, yxc1 = generujPrzeciwny(xxc1, yxc1, p)
    Pm = dodajPktNaKrzywej(A, B, p, xc2, yc2, xxc1, yxc1)
    M = 

print(deszyfruj(38479412483,434747390852,638061376279,629637834291,131275199216,442536171476,21188241970,1515532508))