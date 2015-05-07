def clear2and5(x):
    while x % 2 == 0:
        x = x/2
    while x % 5 == 0:
        x = x/5
    return x


def divides10tonminus1(x):
    n = 1
    val = 9
    while val > 0:
        val = (10*val + 9) % x
        n += 1
    return n


def check(x):
    x = clear2and5(x)
    if x == 1:
        return 0
    return divides10tonminus1(x)

mx = 0
num = 0

for n in range(1, 1000):
    val = check(n)
    if val > mx:
        mx = val
        num = n

print num, mx
