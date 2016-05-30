def isprime(x):
    if x < 2:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1


def check(x):
    n = 0
    diff = x
    while x > 0:
        if isprime(x):
            return 1
        x = x - 2*(2*n + 1)
        n += 1
    return 0


x = 17

while 1:
    if not isprime(x) and not check(x):
        break
    x += 2

print x