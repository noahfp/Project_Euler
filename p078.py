import math

# never mind the old shit, a more intelligent approach is required (generating functions!)

coins = {0:1}
n = 1

while n < 1000000:
	i = 1
	s = 0
	while True: 
		p = i*(3*i-1)/2
		if p > n:
			break
		s += coins[n-p]*(2*(i%2)-1)
		p = i*(3*i+1)/2
		if p > n:
			break
		s += coins[n-p]*(2*(i%2)-1)
		i += 1
	coins[n] = s
	if s % 1000000 == 0:
		print n
		break
	n += 1


