def isprime(x):
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return 0
    return 1

LIMIT = 100000

primes = [x for x in range(2,LIMIT) if isprime(x)]
nps = len(primes)

for a in range(nps):
    i = primes[a]
    for b in range(a+1, nps):
        j = primes[b]
        if isprime(int(str(i)+str(j))) and isprime(int(str(j)+str(i))):
            for c in range(b+1, nps):
                k = primes[c]
                if isprime(int(str(i)+str(k))) and isprime(int(str(j)+str(k))) and isprime(int(str(k)+str(i))) and isprime(int(str(k)+str(j))):
                    for d in range(c+1, nps):
                        l = primes[d]
                        if isprime(int(str(i)+str(l))) and isprime(int(str(j)+str(l))) and isprime(int(str(k)+str(l))) and isprime(int(str(l)+str(i))) and isprime(int(str(l)+str(j))) and isprime(int(str(l)+str(k))):
                            for e in range(d+1, nps):
                                m = primes[e]
                                if isprime(int(str(i)+str(m))) and isprime(int(str(j)+str(m))) and isprime(int(str(k)+str(m))) and isprime(int(str(l)+str(m))) and isprime(int(str(m)+str(i))) and isprime(int(str(m)+str(j))) and isprime(int(str(m)+str(k))) and isprime(int(str(m)+str(l))):
                                    print i+j+k+l+m


