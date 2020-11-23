
from dodawanieLiczb import add
from mnozenieLiczb import multiply
from dzielenieReszta import div
from tobinary import toBinary, makeBinary
from szybkiePotegowanie import exp
from czyModPJestKwad import isModSqr
from tobinary import binaryToDec
from odwrotnosciModN import modinv
from fermat import fermatTest


def main():
    print("1. Algorytm dodawania pisemnego")
    print("2. Algorytm mnożenia pisemnego")
    print("3. Algorytm dzielenia z resztą")
    print("4. Algorytm szybkiego potęgowania")
    print("5. Algorytm sprawdzający czy reszta modulo p jest kwadratem")
    print("6. Algorytm znajdowania odwrotności modulo n")
    print("7. Algorytm testujący złożoność liczby metodą Fermata")
    menuOption = input()
    switcher(menuOption)


def switcher(option):
    if option == '1':
        print("x+y | Podaj x w postaci binarnej")
        x = input()
        print("x+y | Podaj y w postaci binarnej")
        y = input()
        x = makeBinary(x)
        y = makeBinary(y)
        print(x, y, add(x, y))

    elif option == '2':
        print("x*y | Podaj x w postaci binarnej")
        x = input()
        print("x*y | Podaj y w postaci binarnej")
        y = input()
        x = makeBinary(x)
        y = makeBinary(y)
        print(x, y, multiply(x, y))
    elif option == '3':
        print("x/y | Podaj x w postaci binarnej")
        x = input()
        print("x/y | Podaj y w postaci binarnej")
        y = input()
        x = makeBinary(x)
        y = makeBinary(y)
        print(x, y, div(x, y))
    elif option == '4':
        print("(b^k)%n | Podaj n w postaci binarnej")
        n = input()
        print("(b^k)%n | Podaj b w postaci binarnej")
        b = input()
        print("(b^k)%n | Podaj k w postaci binarnej")
        k = input()
        if int(b) < 2 or int(b) > int(n):
            print("b nie spełnia warunku: 2 <= b < n")
            return 0
        print(n, b, k, exp(b, k, n))
    elif option == '5':
        print("Czy reszta modulo p jest kwadrtem? | Podaj p w postaci binarnej")
        p = input()
        print("Czy reszta modulo p jest kwadratem? | Podaj m w postaci binarnej")
        m = input()
        p = makeBinary(p)
        m = makeBinary(m)
        print(p, m, isModSqr(p, m))
    elif option == '6':
        print("Algorytm znajdowania odwrotności modulo n | Podaj a w postaci binarnej")
        a = input()
        print("Algorytm znajdowania odwrotności modulo n | Podaj n w postaci binarnej")
        n = input()
        a, n = makeBinary(a), makeBinary(n)

        if binaryToDec(a) >= binaryToDec(n) or binaryToDec(a) < 0:
            print("a nie spełnia założeń:\n 0 <= a < n")
            return 0
        print(a, n, modinv(a, n))
    elif option == '7':
        print("Algorytm testujący złożoność liczby metodą Fermata | Podaj n w postaci dziesiętnej")
        n = input()
        print("Algorytm testujący złożoność liczby metodą Fermata | Podaj N w postaci dziesiętnej")
        m = input()
        n, m = int(n), int(m)
        if(n < 1):
            print("n powinno być większe od 1")
            return 0
        print(n, m, fermatTest(n, m))
    else:
        print("brak opcji, wybierz ponownie")
        switcher(input())


main()
