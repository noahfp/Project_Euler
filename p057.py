a = 3
b = 2
count = 0

for i in range(1000):
    b = a + b
    a = 2*b - a
    if len(str(a)) > len(str(b)):
        count += 1

print count

