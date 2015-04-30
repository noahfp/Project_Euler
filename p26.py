def clear2and5(x):
    while x%2 == 0:
        x = x/2
    while x%5 == 0:
        x = x/5
    return x

def divides10tonminus1(x):
    n = 1
    while (10**n-1)%x > 0:
        n += 1
    return n

def check(x):
    if divides10ton(x):
        return 0
    return divides10tonminus1(x)

mx = 0
num = 0

for n in range(1,10):
    print n
    val = check(n)
    if val > mx:
        mx = val
        num = n

print num, mx