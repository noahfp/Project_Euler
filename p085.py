import numpy as np

tri = np.array([x*(x+1)/2 for x in range(0,2000)])
mat = np.zeros((2000,2000))
for i in range(2000):
	for j in range(2000):
		mat[i,j] = abs(tri[i]*tri[j] - 2000000)

x = np.argmin(mat)

print x / 2000, x % 2000