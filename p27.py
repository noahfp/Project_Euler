def isprime(x):
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return 0
    return 1

CUTOFF = 1000
maxa = 0
maxb = 0
maxn = 0

for a in range(-CUTOFF+1, CUTOFF):
    for b in range(-CUTOFF+1, CUTOFF):
        n = 0
        while n*n+a*n+b > 1 and isprime(n*n+a*n+b):
            n+=1
        if n > maxn:
            maxa, maxb = a, b
            maxn = n

print maxa*maxb
