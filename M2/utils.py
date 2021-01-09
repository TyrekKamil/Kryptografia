import random

def fermat_test(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(1000):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True
