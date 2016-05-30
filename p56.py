m = 0

for i in range(1,100):
    num = i
    for j in range(1,100):
        m = max(sum([int(char) for char in str(num)]), m)
        num = num*i

print m
