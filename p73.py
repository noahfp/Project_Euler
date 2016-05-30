import math


def gcd(x, y):
	if x < y:
		x = x+y

	if y == 0:
		return x == 1
	return gcd(y, (x % y))


tick = 0

for d in xrange(5,12001):
	print d
	for n in xrange(d/3 + 1, d/2 + 1):
		if gcd(n,d) == 1:
			tick += 1

print tick
