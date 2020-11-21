def div(a, b):
    #    if b > a:
    #        return(0, a)
    a = a[::-1]
    b = b[::-1]
    B = 2
    k = len(a)
    l = len(b)
    r = [0] * (k+1)
    q = [0] * (k+1)

    for i in range(0, k):
        r[i] = a[i]

    for i in range(k - l, -1, -1):
        q[i] = (r[i + l] * B + r[i+l-1]) // (b[l-1])
        if q[i] >= B:
            q[i] = B - 1
        c = 0
        for j in range(0, l):
            tmp = r[i+j]- q[i] * b[j] + c
            c, r[i+j] = Q(tmp, B)
        r[i+l] = r[i+l] + c
        while r[i+l] < 0:
            c = 0
            for j in range(0, l):
                tmp = r[i+j] + b[j] + c
                c, r[i+j] = Q(tmp, B)
            r[i+l] = r[i+l] + c
            q[i] = q[i] - 1
    q = optimize(q)
    r = optimize(r)
    return(q, r)


def Q(x, y):
    return x//y, (x % y)

def optimize(x):
    index = 0
    x = x[::-1]
    for i in range(0, len(x) - 1):
        if(x[i] == 0):
            index = index + 1 
        else: 
            break
    x = x[index:]
    return x

    
