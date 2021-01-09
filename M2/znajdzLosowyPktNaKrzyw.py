from sprawdzCzyPktNalezyDoKrzywej import czyNalezy
from utils import fermat_test
import random

def znajdzLosowyPkt(A, B, p):
    x = random.randint(0, p)
    y = random.randint(0, p) # losowanie x i y z przedziału (0, p) - bez p 

    while not (czyNalezy(A, B, p, x, y)): # warunek punktu krzywej
        x = random.randint(0, p)
        y = random.randint(0, p)
    return A, B, p, x, y


def znajdzlosowyPktMenu(): # kolejność wpisywania danych jest inna niż zaproponowana w dokumencie - wszak A B x y jest zależne od p. 
    print("Algorytm znajdujący losowy punkt na krzywej eliptycznej\n")
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
    print(znajdzLosowyPkt(A, B, p))