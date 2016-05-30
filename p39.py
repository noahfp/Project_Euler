maxm = 0
for p in range(10,1000):
    ticker = 0
    for a in range(1,int(p/3)+1):
        for b in range(a,int(p/2)+1):
            c = p - a - b
            if c*c == a*a + b*b:
                if a + b > c and c > b:
                    print a,b,int(c)
                    ticker += 1
    if ticker > maxm:
        maxm = ticker
        print "CHOOSE:" + str(p)
    print "___"
