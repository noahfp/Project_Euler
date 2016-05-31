import math
from sys import exit
import pprint


def sieve(limit):
    a = [True] * limit                       
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

limit = 71

primes = [x for x in sieve(limit)] 

nprimes = len(primes)

print primes

sums = []
for n in xrange(limit+1):
	sums.append([0]*(nprimes+1))

sums[0] = [1]*(nprimes+1)

for cap in xrange(1, nprimes+1):
	for n in xrange(1, (limit+1)):
		s = 0
		for i in xrange(0, n/primes[cap-1] + 1):
			s = s + sums[n-i*primes[cap-1]][cap-1]
		sums[n][cap] = s

pprint.pprint(sums)

print sums[limit][nprimes]