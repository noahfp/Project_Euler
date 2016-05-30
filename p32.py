s = {1,2,3,4,5,6,7,8,9}

total = set()

for a in s:
    for b in s - {a}:
        for c in s - {a,b}:
            for d in s - {a,b,c}:
                for e in s - {a,b,c,d}:
                    if set(map(int,str((10*a+b)*(100*c+10*d+e)))) == s - {a,b,c,d,e}:
                        if len(str((10*a+b)*(100*c+10*d+e))) == 4:
                            total |= {(10*a+b)*(100*c+10*d+e)}
                    if set(map(int,str((a)*(1000*b+100*c+10*d+e)))) == s - {a,b,c,d,e}:
                        if len(str((a)*(1000*b+100*c+10*d+e))) == 4:
                            total |= {(a)*(1000*b+100*c+10*d+e)}

print sum(total)