def ishex(n):
    k = ((8*n+1)**0.5+1)/4
    return k - int(k) < 0.0000001


def ispent(n):
    k = ((24*n+1)**0.5 + 1)/6
    return k - int(k) < 0.0000001


def trin(n):
    return n*(n+1)/2

i = 286

while 1:
    k = trin(i)
    if ishex(k) and ispent(k):
        print k
        quit()
    i += 1
