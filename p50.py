def isprime(x):
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return 0
    return 1


LIMIT = 1000000

primeslist = list(range(LIMIT))

for i in range(LIMIT):
    if primeslist[i] < 2:
        primeslist[i] = 0
    else:
        j = 2*i
        while j < LIMIT:
            primeslist[j] = 0
            j += i

primeslist = [prime for prime in primeslist if prime > 1]

maxnum = 1

for i in range(22,10000):
    s = sum(primeslist[0:i])
    if s > LIMIT:
        break
    go = 1
    count = 0
    while go:
        if isprime(s): 
            maxnum = s
            go = 0
        s += primeslist[count+i] - primeslist[count]
        if not s < LIMIT:
            go = 0
        count += 1

print maxnum





