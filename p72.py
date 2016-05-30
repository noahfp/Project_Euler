import math

def sumtotient(limit):
	s = 0
	pdiv = primesin(limit)

	for a in xrange(2,limit+1):
		t = a
		for prime in pdiv[a]:
			t = (t/prime)*(prime-1)
		s += t

	return s


def primesin(limit):
	a = {}
	for i in range(limit+1):
		a[i] = []

	primes = sieve(limit)

	for prime in primes:
		for i in range(1,limit/prime+1):
			a[i*prime] = a[i*prime] + [prime]

	return a


def sieve(limit):
    a = [True] * limit                       
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

print sumtotient(1000000)