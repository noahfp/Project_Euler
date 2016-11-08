import math

def sieve(limit):
    a = [True] * limit                       
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

limit = 50000000 
primes = [x for x in sieve(int(math.sqrt(limit))+1)]
primes2 = [x**2 for x in primes if x**2 < limit]
primes3 = [x**3 for x in primes if x**3 < limit]
primes4 = [x**2 for x in primes2 if x**2 < limit]

vals = [0]*limit

for i in primes2:
	for j in primes3:
		for k in primes4:
			if i+j+k < limit:
				vals[i+j+k] = 1

print sum(vals)

