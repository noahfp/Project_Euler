def isprime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1


def circle(x):
    c = []
    x = str(x)
    for i in range(len(str(x))):
        c.append(int(x[i:len(x)]+x[0:i]))
    return c

for i in range(2,1000000):
    yea = 1
    for x in circle(i):
        if not isprime(x):
            yea = 0
            break
    if yea:
        print i


