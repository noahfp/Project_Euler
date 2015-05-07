def addup(x):
    return x*(x+1)/2


def incl_excl(mults):
    cols = []
    for i in range(1, 2**len(mults)):
        col = []
        for j in range(len(mults)):
            if i & 2**j > 0:
                col.append(mults[j])
        cols.append(col)
    return cols


def gcd(x, y):
    if x < y:
        x = x+y
        y = x-y
        x = x-y
    if y == 0:
        return x
    return gcd(y, (x % y))


def lcm(col):
    val = 1
    for num in col:
        val = val*num/gcd(val, num)
    return val


def sum_mult_to_n(n, mults):
    total = 0
    cols = incl_excl(mults)
    for col in cols:
        lcmp = lcm(col)
        total += addup((n-1)/lcmp)*lcmp*((-1)**(len(col)-1))
    return total


print sum_mult_to_n(int(raw_input("")), map(int, raw_input("").split()))
