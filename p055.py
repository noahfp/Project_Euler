def ispalindrome(x):
    return str(x) == str(x)[::-1]


def revadd(x):
    return int(x) + int(str(x)[::-1])


def count(x, i):
    if i > 50:
        return 0
    x = revadd(x)
    if ispalindrome(x):
        return 1
    return count(x, i+1)


lychrel = 0

for i in range(10000):
    lychrel += 1-count(i,0)

print lychrel