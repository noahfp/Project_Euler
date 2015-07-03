def isprime(x):
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return 0
    return 1

def tr(n):
    return (2*n)*(2*n-1)+1

def tl(n):
    return (2*n)**2 + 1

def bl(n):
    return (2*n)*(2*n+1)+1


count = 1.0
primes = 0.0
i = 0

while primes/count > 0.1 or i == 0:
    i += 1
    count += 4
    if isprime(tr(i)):
        primes += 1
    if isprime(tl(i)):
        primes += 1
    if isprime(bl(i)):
        primes += 1

print (2*i+1)