import math

def relprime(a,b):
	if b > a:
		temp = a
		a = b
		b = temp

	while b > 0:
		a,b = relprimeiter(a,b)

	return a == 1


def relprimeiter(a,b):
	return b, a % b

m = 0
nmax = 0

for d in xrange(1000000):
	if not d % 7 == 0:
		n = 3*d/7
		if relprime(n,d):
			if n/float(d) > m:
				m = n/float(d)
				nmax = n
				print n