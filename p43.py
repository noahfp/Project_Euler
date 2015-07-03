def isprime(x):
    if x < 2:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1


def perms(nums):
    list = []
    if len(nums) == 1:
        return [nums[0]]
    item = nums.pop()
    n = len(nums)
    for perm in perms(nums):
        for i in range(n+1):
            list.append(perm[0:i]+item+perm[i:n])
    return list


nums = ['1','2','3','4','5','6','7','8','9','0']
list = []

for num in perms(nums):
    if int(num[1:4]) % 2 == 0:
        if int(num[2:5]) % 3 == 0:
            if int(num[3:6]) % 5 == 0:
                if int(num[4:7]) % 7 == 0:
                    if int(num[5:8]) % 11 == 0:
                        if int(num[6:9]) % 13 == 0:
                            if int(num[7:10]) % 17 == 0:
                                print int(num)
                                list.append(int(num))

print "___"
print sum(list)


