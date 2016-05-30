from collections import Counter
import math

def isperm(x, y):
    return Counter(str(x)) == Counter(str(y))


def distinct(*args):
    n = len(args)
    for i in range(n):
        for j in range(i+1,n):
            if args[i] == args[j]:
                return 0
    return 1

# returns cubes with n digits
def cubes(n):
    return [i**3 for i in range(int(math.ceil(math.pow(10,(n-1)/3.0))), int(math.ceil(math.pow(10,n/3.0))))]

# n = 12
# countercounter = Counter([str(Counter(str(cube))) for cube in cubes(n)])
# for counter in countercounter:
#     if countercounter[counter] == 5:
#         print counter

for cube in cubes(12):
    if Counter(str(cube)) == Counter("012334566789") or Counter(str(cube)) == Counter("012334556789"):
        print cube


