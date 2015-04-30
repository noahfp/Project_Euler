day = 1
counter = 0

for year in range(1901,2001):
    if year % 4 == 0:
        m = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        m = [31,28,31,30,31,30,31,31,30,31,30,31]
    for mon in range(12):
        if day % 7 == 0:
            counter += 1
        day = day + m[mon] % 7

print counter