def pent(n):
    return n*(3*n-1)/2


def ispent(n):
    n = 2*n
    k = int((n/3)**0.5)+1
    return k*(3*k-1) == n:


sat = 0
r = 1

while sat < 2:
    pentr = pent(r)
    for m in range(1, r/2 + 1, 2):
        if ispent(pentr - 3*m*r + m) and ispent(pentr - 3*m*r + 3*m**2):
            sat += 1
            print pentr - (3*m*r-m)/2, pent(m), pent(r-m), pentr - 3*m*r + 3*m**2
    r += 1


quit()


while not sat:
    j = i
    while pent(j+1) - pent(j) < pent(i)+1:
        if ispent(pent(j) + pent(i)):
            print "CHECK"
            if ispent(2*pent(j) + pent(i)) or ispent(pent(j) + 2*pent(i)):
                print "DOUBLECHECK"
                sat = 1

        j += 1
    print pent(i) 
    i += 1
