from collections import Counter

def isperm(x,y):
    return Counter(str(x)) == Counter(str(y))

for i in range(1,10000000):
    if isperm(i, 2*i) and isperm(i, 3*i) and isperm(i, 4*i) and isperm(i, 5*i) and isperm(i, 6*i):
        print i
        break