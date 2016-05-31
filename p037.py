def isprime(x):
    if x < 2:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1

def check(x):
    ch = True
    if not isprime(x):
        return False
    x = str(x)
    for i in range(1,len(x)):
        if not isprime(int(x[i:])) or not isprime(int(x[:i])):
            ch = False
            break
    return ch

total = 0
list = []
i = 11

while total < 11:
    if check(i):
        list.append(i)
        total += 1
    i += 1

print list
print sum(list)


