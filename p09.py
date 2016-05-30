# problem reduces to solving 2*1000^2-4*1000k+k^2-(k-2a)^2=0, where 
# k = a+b. Hence, we just need 2k to divide 1000^2, and
# the result to be some number between 0 and k.

n = int(raw_input(""))

for k in range(1,n):
    for a in range(1,k/2+1):
        if 2*a*(a-k) == n*(n-2*k):
            print a, k-a, n-k
            print a*(k-a)*(n-k)

