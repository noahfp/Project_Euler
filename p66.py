import math

def cf(n):
	if math.floor(math.sqrt(n))**2 == n:
		return 0
	else:
		a = math.floor(math.sqrt(n))
		b = 1
		arr = [a]
		while 1:
			shell = cfiter(n,a,b)
			val,a,b = shell[0],shell[1],shell[2]
			if b == 1:
				break
			arr.append(val)
		return arr

def cfiter(n, a, b):
	bnew = (n-a*a)/b
	val = math.floor((math.sqrt(n)+a)/bnew)
	anew = val*bnew - a
	return [val,anew,bnew]

def frac(arr):
	if len(arr) == 1:
		return [arr[0], 1.0]
	c = arr.pop()
	a = arr.pop()
	b = 1
	while 1:
		if len(arr) == 0:
			return [a*c + b,c]
		else:
			temp = c
			c = a*c + b
			b = temp
			a = arr.pop()

def pell(D):
	arr = cf(D)
	l = len(arr)
	frc = frac(arr)
	p,q = frc[0], frc[1]
	if l % 2:
		p = p**2 + D*(q**2)
	return p

cap = 1000
maxx = 0
maxD = 0

for D in xrange(2,cap+1):
	if not D == math.floor(math.sqrt(D))**2:
		x = pell(D)
		if x > maxx:
			maxx = x
			maxD = D
			print D,x




	
