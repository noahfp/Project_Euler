def fact(n):
    total = 1
    while n > 1:
        total = n*total
        n = n - 1
    return total


def facdigitsum(n):
    return sum([fact(int(c)) for c in str(n)])


for i in range(10,10000000):
    if facdigitsum(i) == i:
        print i

