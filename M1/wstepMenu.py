
from dodawanieLiczb import add
from mnozenieLiczb import multiply
from dzielenieReszta import div
from tobinary import toBinary, makeBinary
from szybkiePotegowanie import exp


def main():
    print("1. Dodawanie\n2. Mnozenie\n3. Dzielenie z resztą\n4. Szybkie potęgowanie")
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
        print("(b^k)%n | Podaj b w postaci dziesiętnej")
        b = input()
        print("(b^k)%n | Podaj k w postaci dziesiętnej")
        k = input()
        print("(b^k)%n | Podaj n w postaci dziesiętnej")
        n = input()
        if int(b) < 2 or int(b) > int(n):
            print("b nie spełnia warunku: 2 <= b < n")
            return 0
        b = toBinary(b)
        k = toBinary(k)
        n = toBinary(n)
        print(b, k, exp(b, k, n))
    else:
        print("brak opcji, wybierz ponownie")
        switcher(input())


main()
