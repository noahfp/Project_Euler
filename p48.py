def powermod(x,y,m):
    val = 1
    for i in range(y):
        val = val*x % m
    return val

print sum([powermod(x,x,10000000000) for x in range(1,1001)]) % 10000000000
