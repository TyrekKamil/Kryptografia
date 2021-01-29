from utils import HexToBin, BinToHex, losujF, RandomHex

def dodaj(xy, uw):
    xy = HexToBin(xy)
    while len(xy) < 8:
        xy.insert(0, 0)
    x = xy[:4]
    y = xy[4:]

    uw = HexToBin(uw)
    while len(uw) < 8:
        uw.insert(0, 0)
    u = uw[:4]
    w = uw[4:]

    a, b = [], []
    for i in range(0,4):
        digitA = (int(x[i]) + int(u[i])) % 2
        digitB = (int(y[i]) + int(w[i])) % 2
        a.append(str(digitA))
        b.append(str(digitB))
    return (str(BinToHex(a)) + str(BinToHex(b))).upper()


def Zad1():
    xy = RandomHex()
    uw = RandomHex()
#    xy = "4B"
#    uw = "B2"
    f = losujF()
    print(xy, uw, dodaj(xy, uw), f)

def przykladoweWejscia():
    file1 = open('./Wejscia/Zad1.txt', 'r')
    Lines = file1.readlines() 
    a, b, c = [], [], []
    for line in Lines:
        arr = line.split(",")
        arr[2] = arr[2].strip()
        a.append(arr[0])
        b.append(arr[1])
        c.append(arr[2])
        print(arr[0], arr[1], dodaj(arr[0], arr[1]), " Czy wynik się zgadza?", arr[2] == dodaj(arr[0], arr[1]))

#przykladoweWejscia()
#Zad1()
#dodaj()