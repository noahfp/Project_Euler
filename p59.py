from collections import Counter

datafile = open('data59.txt','r')

data = map(int, datafile.readline().split(","))

count = 0
d = [[],[],[]]

for num in data:
    d[count].append(num)
    count += 1
    count = count % 3

cracked = [[],[],[]]

for i in range(3):
    m = 0
    for key in range(97,123):
        s = d[i]
        a = []
        for j in range(len(s)):
            a.append(s[j] ^ key)
        acount = dict(Counter(a))
        try:
            acount[32]
        except KeyError:
            a32 = 0
        else:
            a32 = acount[32]
        if a32 > m:
            cracked[i] = a
            m = a32

stitch = []

for i in range(len(data)):
    stitch.append((cracked[i%3][i/3]))

print sum(stitch)



