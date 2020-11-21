from mnozenieLiczb import multiply
from tobinary import toBinary
from dzielenieReszta import div

def main():
    x,z=6977, 3641
    y = (z-1)//2 
    print(toBinary(pow(x,y,z)))

    b = toBinary(x) 
    k = toBinary(y)
    n = toBinary(z)
    print(b,k,n)
    print(exp(b, k, n))

def exp(b, k, n):
    r = [1] 
    x = div(b, n)[1]
    
    for i in range(len(k) - 1, -1, -1):
        if k[i] == 1:
            r = multiply(r, x)
            r = div(r, n)[1]
        x  = multiply(x, x)
        x  = div(x, n)[1]
    return r

main()