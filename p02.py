def evenfib(n,p1,p2,d):
    total = 0
    if p1%d == 0:
        total += p1
    while p2 < n:
        t = p2
        p2 = p1+p2
        p1 = t
        if p1 % 2 == 0:
            total += p1
    return total

print evenfib(*(map(int,raw_input("").split())))