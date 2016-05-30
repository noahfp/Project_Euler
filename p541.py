import math

def gcd(a,b):
	if a < b:
		a = a + b

	while b > 0:
		temp = a
		a = b
		b = temp % a

	return a

def update(a,b,n):
	anew = a*n + b
	bnew = b*n
	div = gcd(anew,bnew)
	anew = anew/div
	bnew = bnew/div
	return anew, bnew

a = b = 1
for n in range(1,10000):
	print n,a,b
	a,b = update(a,b,n)