from math import factorial as fac

def fsum(n):
	s = 0
	for d in str(n):
		s += fac(int(d))
	return s

def loop(n):
	count = 0
	nums = set([])
	while not n in nums:
		nums.add(n)
		n = fsum(n)
		count += 1
	return count

tick = 0
for n in xrange(1000000):
	if loop(n) == 60:
		tick += 1
		print n

print tick