def pfac(x,cap):
    dic = dict()
    if x == 1:
        return dic
    if cap > int(x**(0.5)):
        dic[x] = 1
        return dic
    for i in range(cap,int(x**(0.5))+1):
        if x % i == 0:
            counter = 0
            while x % i == 0:
                x = x/i
                counter += 1
            dic[i] = counter
            return dict(dic,**(pfac(x,i+1)))
    dic[x] = 1
    return dic

def divisorsum(x):
    if x == 1:
        return 1
    primes = pfac(x,2)
    prod = 1
    for p in primes.keys():
        prod = prod*(p**(primes[p]+1)-1)/(p-1)
    return prod - x

list = []

for x in range(10000):
    y = divisorsum(x)
    if not y == x:
        if divisorsum(y) == x:
            list.append(x)

print sum(list)