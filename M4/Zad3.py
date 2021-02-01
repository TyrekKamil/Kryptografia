from utils import HexToBin, BinToHex, losujF, RandomHex
from Zad2 import xTime
from Zad1 import dodaj

def pomnoz(xy, uw, c):
    xy = HexToBin(xy)
    while len(xy) < 8:
        xy.insert(0, 0)  # uzupełnienie zer aby bylo 8

    uw = HexToBin(uw)
    while len(uw) < 8:
        uw.insert(0, 0)

    xTimeArr = []

    # generowanie xtime
    for i in range(1, 8):
        tmp = BinToHex(xy)
        for j in range(1, i + 1):
            tmp = xTime(tmp, c)
        xTimeArr.append(tmp)

    result = BinToHex(['0'])
    xy = xy[::-1]
    uw = uw[::-1]
    c = c[::-1]
  #  uw = [int(x) for x in uw]

    for i in range(7, 1, -1):
        if uw[i] == '1':
            tmp = dodaj(BinToHex(uw[i-1]), xTimeArr[i - 1])
            result = dodaj(result, tmp)
    if uw[0] == '1':
        result = dodaj(result, BinToHex(xy[::-1]))
    return result.upper()

def Zad3():
    xy = RandomHex()
    uw = RandomHex()
    f = losujF()
    f = [1, 0, 0, 1, 0, 1, 1, 0, 1]
    xy, uw = "df", "88"
    print(xy, uw, pomnoz(xy, uw, f), f)


def przykladoweWejscia():
    file1 = open('Wejscia/zad3.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        arr = line.split(";")

        arr[3] = arr[3].strip().replace(" ", "")
        arr[3] = arr[3][1:-1]
        arr[3] = arr[3].split(",")
        arr[3] = [int(x) for x in arr[3]]
        print(arr[0], arr[1], pomnoz(arr[0], arr[1], arr[3]), arr[3],
              " Czy wynik się zgadza?", arr[2] == pomnoz(arr[0], arr[1], arr[3]), arr[2])


przykladoweWejscia()
Zad3()
