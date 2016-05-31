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


nums = ['1','2','3','4','5','6','7']
cap = 0
for num in perms(nums):
    num = int(num)
    if isprime(num):
        if num > cap:
            cap = num
            print num

print cap