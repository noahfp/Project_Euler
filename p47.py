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

def hasnumdivs(x, n):
    i = 2
    divs = 0
    while divs < n + 1 and x > i - 1:
        if x % i == 0:
            divs += 1
            while x % i == 0:
                x = x/i
        i += 1
    if divs == n:
        return 1
    return 0

i = 17

while 1:
    if hasnumdivs(i, 4):
        if hasnumdivs(i+1, 4):
            if hasnumdivs(i+2, 4):
                if hasnumdivs(i+3, 4):
                    print i
                    quit()
            i += 1
        i += 1
    i += 1
