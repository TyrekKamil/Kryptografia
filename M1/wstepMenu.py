
from dodawanieLiczb import add
from mnozenieLiczb import multiply
from dzielenieReszta import div
from tobinary import toBinary, makeBinary
from szybkiePotegowanie import exp
from czyModPJestKwad import isModSqr

def main():
    print("1. Algorytm dodawania pisemnego\n2. Algorytm mnożenia pisemnego\n3. Algorytm dzielenia z resztą\n4. Algorytm szybkiego potęgowania\n5. Algorytm sprawdzający czy reszta modulo p jest kwadratem")
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
        print(isModSqr(p, m))

    else:
        print("brak opcji, wybierz ponownie")
        switcher(input())


main()
