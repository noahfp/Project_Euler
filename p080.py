from math import sqrt, floor

def sqt(n,d):
	s = str(long(floor(sqrt(n))))
	d = d - len(s)
	for i in range(d):
		sub = 0
		for b in range(10):
			k = s + str(b)
			if long(k)**2 > 100L*n*10**(2*i):
				sub = 1
				break
		b = b - sub
		s = s + str(b)
	return s

s = 0

for i in range(1,101):
	if not floor(sqrt(i))**2 == i:
		k = sum([int(x) for x in sqt(i,100)])
		s += k
		print k

print s

