from utils import HexToBin, BinToHex, losujF, RandomHex


def xTime(ab, c):
    x = "02"
    x = HexToBin(x)
    while len(x) < 8:
        x.insert(0, 0)  # uzupełnienie zer aby bylo 8

    ab = HexToBin(ab)
    while len(ab) < 8:
        ab.insert(0, 0)
    result = []
    if int(ab[0]) == 1:
        ab = ab[::-1]
        c = c[::-1]
        for i in range(7, 0, -1):
            tmp = (c[i] + int(ab[i-1])) % 2
            result.append(str(tmp))
        result.append(c[0])
    elif int(ab[0]) == 0:
        result = ab[1:]
        while len(result) < 8:
            result.append(str(0))

    result = [str(x) for x in result]
    return BinToHex(result).upper()
# 92 1001 0010
# 11 0001 0001
# 3f 0011 1111

def Zad2():
    ab = RandomHex()
    f = losujF()
    ab = "92"
    f = [1, 0, 0, 0, 1, 1, 0, 1, 1]
    print(ab, xTime(ab, f), f)

def przykladoweWejscia():
    file1 = open('Wejscia/zad2.txt', 'r')
    Lines = file1.readlines() 

    for line in Lines:
        arr = line.split(";")

        arr[2] = arr[2].strip()
        arr[2] = arr[2][1:-1]
        arr[2] = arr[2].split(",")
        arr[2] = [int(x) for x in arr[2]]

        print(arr[0], xTime(arr[0], arr[2]), arr[1], " Czy wynik się zgadza?", arr[1] == xTime(arr[0], arr[2]))

#przykladoweWejscia()
#Zad2()