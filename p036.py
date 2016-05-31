def ispalindrome(x):
    x = str(x)
    if x[::-1] == x:
        return 1
    return 0


def binr(x):
    val = ""
    while x > 0:
        if x % 2 == 0:
            val += "0"
        else:
            val += "1"
        x = x/2
    return val[::-1]


list = []
for x in range(1,1000000):
    if ispalindrome(x) and ispalindrome(binr(x)):
        list.append(x)

print sum(list)