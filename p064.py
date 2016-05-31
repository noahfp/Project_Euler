import math

def cf(n):
	if int(math.sqrt(n))**2 == n:
		return 0
	else:
		count = 1
		a = math.floor(math.sqrt(n))
		b = 1
		while 1:
			shell = cfiter(n,a,b)
			val,a,b = shell[0],shell[1],shell[2]
			if b == 1:
				break
			count += 1
		return count % 2

def cfiter(n, a, b):
	bnew = (n-a*a)/b
	val = math.floor((math.sqrt(n)+a)/bnew)
	anew = val*bnew - a
	return [val,anew,bnew]

s = 0

for n in range(1,10001):
	s += cf(n)
	print n

print s

