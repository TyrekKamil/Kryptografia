from generowanieLosowejKrzywejElip import generLosowejMenu
from znajdzLosowyPktNaKrzyw import znajdzlosowyPktMenu
from sprawdzCzyPktNalezyDoKrzywej import sprawdzCzyPktNalezy_menu
from generujElementPrzeciwny import generujMenu
from DodajDwaPunktyNaKrzywej import DodajPunktyMenu


def main():
    menuOption = input("Wybierz program:\n1. Algorytm generujący losową krzywą eliptyczną\n2. Algorytm znajdujący losowy punkt na krzywej eliptycznej\n3. Algorytm sprawdzający czy punkt należy do krzywej\n4. Algorytm generujący element przeciwny do zadanego\n5. Algorytm który dodaje dwa zadane punkty na krzywej eliptycznej\n")
    switcher(menuOption)


def switcher(option):
    if option == "1":
        generLosowejMenu()
    elif option == "2":
        znajdzlosowyPktMenu()
    elif option == "3":
        sprawdzCzyPktNalezy_menu()
    elif option == "4":
        generujMenu()
    elif option == "5":
        DodajPunktyMenu()
    else:
        print("brak opcji, wybierz ponownie")
        switcher(input())


main()
