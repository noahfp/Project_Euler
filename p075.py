import math

def gcd(x, y):
	if x < y:
		x = x+y

	if y == 0:
		return x == 1
	return gcd(y, (x % y))

d = {}
limit = 1500000

for i in range(1,limit+1):
	d[i] = 0

for m in range(2,int(math.sqrt(limit))):
	for n in range(1, m):
		if gcd(m,n) == 1 and (m - n) % 2 == 1:
			C = 2*m*(m+n)
			if C > limit:
				break
			else:
				for k in xrange(1,limit/C + 1):
					d[k*C] += 1
					

print sum([1 for x in d.values() if x == 1])