import math
from collections import Counter

def sieve(limit):
    a = [True] * limit                       
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False


def phi(n):
	pass

primes = [value for value in sieve(10000000)]

print len(primes)
minr = 10000
minx = 0
miny = 0

for x in primes:
	if x > 3300:
		break
	for y in primes:
		if x*y > 10000000:
			break
		if not x == y:
			if Counter(str(x*y)) == Counter(str((x-1)*(y-1))):
				r = (x+y-1)/float(x*y)
				if r < minr:
					minr = r
					minx,miny = x,y
					print r,x,y
