from utils import fermat_test

def dodajPktNaKrzywej(A, B, p, x1, y1, x2, y2):
    # Przypadek P = -Q
    if (x1, y1) == (x2, ((-1*y2) % p)):
        return A, B, p, x1, y1, x2, y2, "inf", "inf"
    # Przypadek P != Q
    elif (x1) != (x2):
        lam = ((y2 - y1) * (pow((x2 - x1), -1, p))) % p
        x3 = (pow(lam, 2) - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return A, B, p, x1, y1, x2, y2, x3, y3
    # Przypadek P = Q
    elif (x1, y1) == (x2, y2):
        lam = (((3 * pow(x1, 2)) + A) * (pow((2 * y1), -1, p))) % p
        x3 = (pow(lam, 2) - 2 * x1) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return A, B, p, x1, y1, x2, y2, x3, y3

def DodajPunktyMenu():
    print("Algorytm który dodaje dwa zadane punkty na krzywej eliptycznej\n")
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

    x1 = input("Liczba x1 mniejsza od p - 1\n")
    x1 = int(x1)
    while (x1 > p - 1 or x1 < 0): # warunek dla x1
        B = input("Liczba x1 musi spełnić waurnek B < p - 1\n")
        B = int(B)

    y1 = input("Liczba y1 mniejsza od p - 1\n")
    y1 = int(y1)
    while (y1 > p - 1 or y1 < 0): # warunek dla y
        y1 = input("Liczba y1 musi spełnić waurnek y < p - 1\n")
        y1 = int(y1)

    x2 = input("Liczba x2 mniejsza od p - 1\n")
    x2 = int(x2)
    while (x2 > p - 1 or x2 < 0): # warunek dla x2
        B = input("Liczba x2 musi spełnić waurnek B < p - 1\n")
        B = int(B)

    y2 = input("Liczba y2 mniejsza od p - 1\n")
    y2 = int(y2)
    while (y2 > p - 1 or y2 < 0): # warunek dla y2
        y2 = input("Liczba y2 musi spełnić waurnek y2 < p - 1\n")
        y2 = int(y2)
    print(dodajPktNaKrzywej(A, B, p, x1, y1, x2, y2))