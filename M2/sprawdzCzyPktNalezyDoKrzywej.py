import random
from utils import fermat_test

def czyNalezy(A, B, p, x, y):
    result = False # kontrolka - domyslnie false, przy spełnionym warunki TRUE
    if ((y**2) % p) == ((x**3 + A*x + B) % p): # y2 = x3 + Ax + B oraz p jako modulo
        return True
    return A, B, p, x, y, result

def sprawdzCzyPktNalezy_menu(): # kolejność wpisywania danych jest inna niż zaproponowana w dokumencie - wszak A B x y jest zależne od p. 
    p = input("Liczba pierwsza p spełniająca warunek 3 mod 4\n")
    p = int(p)
    while (p % 4 != 3 or p < 0 or not fermat_test(p)): # warunek pod liczbę p: p = 3 mod 4
        p = input("Liczba p musi spełnić waurnek 3 mod 4\n")
        p = int(p)

    A = input("Liczba A mniejsza od p - 1\n")
    A = int(A)
    while (A > p - 1 or A < 0): # warunek dla A < p -1
        A = input("Liczba A musi spełnić waurnek A < p - 1\n") 
        A = int(A)

    B = input("Liczba B mniejsza od p - 1\n")
    B = int(B)
    while (B > p - 1 or B < 0): # warunek dla B
        B = input("Liczba B musi spełnić waurnek B < p - 1\n")
        B = int(B)

    x = input("Liczba x mniejsza od p - 1\n")
    x = int(x)
    while (x > p - 1 or x < 0): # warunek dla x
        B = input("Liczba x musi spełnić waurnek B < p - 1\n")
        B = int(B)

    y = input("Liczba y mniejsza od p - 1\n")
    y = int(y)
    while (y > p - 1 or y < 0): # warunek dla y
        y = input("Liczba y musi spełnić waurnek y < p - 1\n")
        y = int(y)
    print(czyNalezy(A, B, p, x, y))
