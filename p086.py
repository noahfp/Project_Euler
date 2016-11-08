import math
import numpy as np 

def triples(limit):
	ans = []
	for m in xrange(1,int(math.floor(math.sqrt(2*limit+1)))+1):
		for n in xrange(1, m):
			if (n + m) % 2 == 1:
				a, b = max(m**2 - n**2, 2*m*n), min(m**2 - n**2, 2*m*n)
				for i in xrange(1, min(limit*2//a,limit//b)+1):
					ans.append([a*i,b*i])
	return ans

def cubes(a,b,limit):
	ans = 0
	if not a > limit:
		ans += b//2
	if not b > limit:
		M = b
		m = a-a//2
		ans += max(0, M-m+1)
	print a,b,limit,ans
	return ans

def check(limit):
	return sum([cubes(x[0],x[1],limit) for x in triples(limit)])

# UGH FIGURE THIS SHIT OUT
limit = 10

print triples(limit)
print check(limit)

