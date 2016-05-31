list

for i in range(10,100):
    for j in range(10,100):
        a = i/10
        b = i % 10
        c = j/10
        d = j % 10
        if a == d and i*c == b*j and not i == j:
            print i,j
