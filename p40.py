def finddigit(x):
    n = 1
    while x > n*(10**n - 10**(n-1)):
        x -= n*(10**n - 10**(n-1))
        n += 1
    num = 10**(n-1) + (x-1)/n
    return int(str(num)[(x - 1) % n])


list = []
prod = 1

for i in range(7):
    list.append(finddigit(10**i))
    prod = prod*finddigit(10**i)

print list 
print prod