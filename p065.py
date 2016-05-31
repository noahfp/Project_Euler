import math

def frac(arr):
	c = arr.pop()
	a = arr.pop()
	b = 1
	while 1:
		if len(arr) == 0:
			return a*c + b
		else:
			temp = c
			c = a*c + b
			b = temp
			a = arr.pop()

def earr(n):
	n += -1 
	arr = [2]
	mod = 0
	count = 2
	while n > 0:
		arr += [1,count,1]
		count += 2
		n += -3
	return arr

print sum([int(ch) for ch in str(frac(earr(100)))])







