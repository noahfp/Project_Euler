def check(x):
    x = str(x)
    fail = 1
    for i in range(1,10):
        if not str(i) in x:
            fail = 0
            break
    return fail

for i in range(9183,10000):
    if check(str(i)+str(2*i)):
        print i

print "done"