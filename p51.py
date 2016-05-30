def isprime(x):
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return 0
    return 1


def arrs(n, x):
    if n == 0:
        arr = ''
        for i in range(x):
            arr += 'x'
        return [arr]
    elif x == 0:
        arr = ''
        for i in range(n):
            arr += 'n'
        return [arr]
    else:
        return [arr+'x' for arr in arrs(n, x-1)] + [arr+'n' 
            for arr in arrs(n-1, x)]


def verify(n, x, rem):
    if not len(str(rem)) == n:
        return "ERROR"
    for arr in arrs(n, x):
        nums = []
        for i in range(1,10):
            r = list(str(rem))[::-1]
            num = ''
            for j in range(n+x):
                if arr[j] == 'x':
                    num += str(i)
                else:
                    num += r.pop()
            nums.append(num)
        nnums = []
        for num in nums:
            if isprime(int(num)):
                nnums.append(int(num))
        if len(nnums) > 7:
            print nnums


for i in range(1000):
    verify(len(str(i)), 3, i)


