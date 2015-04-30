LIM = int(raw_input(""))

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

abun = []

for i in range(3,LIM):
    if divisorsum(i) > i:
        abun.append(i)

nsummable = [1,2,3,4,5,6]

for n in range(7,LIM):
    fail = 1
    i = 0
    j = len(abun)-1
    while i<j+1 and fail == 1:
        if abun[i]+abun[j] == n:
            fail = 0
        elif abun[i]+abun[j] < n:
            i += 1
        else:
            j -= 1
    if fail == 1:
        nsummable.append(n)
        print n

print sum(nsummable) 