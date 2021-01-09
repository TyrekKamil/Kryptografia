from utils import fermat_test

def generujPrzeciwny(p, x, y):
    return p, x, y, (x % p), (-1 * y % p) # zgodnie z warunkiem - x1 (czwarta wartość) to x mod p, y1 to -y mod p


def generujMenu():
    p = input("Liczba pierwsza p spełniająca warunek 3 mod 4\n")
    p = int(p)
    while (p % 4 != 3 or p < 0 or not fermat_test(p)): # warunek pod liczbę p: p = 3 mod 4
        p = input("Liczba p musi spełnić waurnek 3 mod 4\n")
        p = int(p)
    
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
    print(generujPrzeciwny(p, x, y))