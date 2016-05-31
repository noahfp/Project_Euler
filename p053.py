def fact(x, y):
    val = 1
    for i in range(x+1, y+1):
        val = val*(i)
    return val


def comb(n, r):
    return fact(n-r, n)/fact(0,r)


counter = 0

for i in range(1,101):
    for j in range(0,i+1):
        if comb(i, j) > 1000000:
            counter += 1

print counter