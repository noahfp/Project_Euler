from collections import Counter

def isprime(x):
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return 0
    return 1

def isperm(x,y):
    return Counter(str(x)) == Counter(str(y))


for i in range(1000, 10000):
    if isprime(i):
        for skip in range(1, (10000 - i)/2):
            if isperm(i, i + skip) and isperm(i, i+2*skip):
                if isprime(i+skip) and isprime(i+2*skip):
                    print i, i+skip, i+2*skip
