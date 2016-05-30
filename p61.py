def polyn(p, n):
    return n*((p-2)*n-(p-2)+2)/2

arr = dict([])
arrn = dict([])

for p in range(3,9):
    arr[p] = set([polyn(p, n) for n in range(200) if polyn(p, n) > 999 and polyn(p, n) < 10000])
    dummy = dict([])
    for num in arr[p]:
        if not int(str(num)[0:2]) in dummy.keys():
            dummy[int(str(num)[0:2])] = set([int(str(num)[2:4])])
        else:
            dummy[int(str(num)[0:2])] |= set([int(str(num)[2:4])])
    arrn[p] = dummy

call = set([4,5,6,7,8])

for primer in arrn[3]:
    for a in arrn[3][primer]:
        for numa in set(call):
            if a in arrn[numa]:
                call.discard(numa)
                for b in arrn[numa][a]:
                    for numb in set(call):
                        if b in arrn[numb]:
                            call.discard(numb)
                            for c in arrn[numb][b]:
                                for numc in set(call):
                                    if c in arrn[numc]:
                                        call.discard(numc)
                                        for d in arrn[numc][c]:
                                            for numd in set(call):
                                                if d in arrn[numd]:
                                                    call.discard(numd)
                                                    for e in arrn[numd][d]:
                                                        for nume in set(call):
                                                            if e in arrn[nume]:
                                                                call.discard(nume)
                                                                for f in arrn[nume][e]:
                                                                    if f == primer:
                                                                        print int(str(f) + str(a)) + int(str(a) + str(b)) + int(str(b) + str(c)) + int(str(c) + str(d)) + int(str(d) + str(e)) + int(str(e) + str(f)), str(f) + str(a), str(a) + str(b), str(b) + str(c), str(c) + str(d), str(d) + str(e), str(e) + str(f)
                                                                call.add(nume)
                                                    call.add(numd)
                                        call.add(numc)
                            call.add(numb)
                call.add(numa)
