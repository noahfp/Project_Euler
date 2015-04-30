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



print max(pfac(int(raw_input("")),2).keys())
