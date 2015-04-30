def gcd(x,y):
    if x < y: 
        x = x+y
        y = x-y
        x = x-y
    if y == 0:
        return x
    return gcd(y,(x % y))

def lcm(col):
    val = 1
    for num in col:
        val = val*num/gcd(val,num)
    return val

print lcm(range(1,20))