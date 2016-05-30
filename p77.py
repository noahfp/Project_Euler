import math


limit = 100 

sums = []
for i in xrange(limit+1):
	sums.append([0]*(limit+1))

sums[0] = [1]*limit
for i in xrange((limit+1)):
	sums[i][1] = 1

for cap in xrange(2, (limit+1)):
	for n in xrange(1, (limit+1)):
		s = 0
		for i in xrange(0, n/cap + 1):
			s = s + sums[n-i*cap][cap-1]
		sums[n][cap] = s

print sums[100][99]