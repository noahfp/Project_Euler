l = []

for i in range(10,500000):
    a = [int(c)**5 for c in str(i)]
    if sum(a) == i:
        l.append(i)

print l
print sum(l)