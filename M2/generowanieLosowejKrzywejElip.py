from random import randint
from utils import fermat_test

def gen(p):
    result = False # flaga, której końcowa wartość definuje, czy z danych wartości stworzymy krzywą eliptyczną
    while result == False: # dopóki jest false...
        A = randint(0, p)
        B = randint(0, p) # losowe A B
        delta = (4 * pow(A, 3) + 27 * pow(B, 2)) % p # warunek 4A3 + 27B2 = 0 (mod p)
        if delta != 0: # jeśli nie jest równe, para spełnia warunek - true
            result = True
    return A, B, delta 

def generLosowejMenu():
    print("Algorytm generujący losową krzywą eliptyczną\n")
    MAX_VALUE = 1000000000 # największa wartość p do wylosowania 
    p = 2 # wartość początkowa, aby pętla while załapała
    while not (fermat_test(p) is False and p % 4 == 3): # fermat_test z pakietu utils weryfikuje, czy liczba jest pierwsza, dodatkowo warunek p%4==3
        p = randint(1, MAX_VALUE) # losowanie dopoki nie spelni warunkow
    print(gen(p)) 