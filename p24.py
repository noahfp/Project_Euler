def factorial(x):
    val = 1
    for i in range(x):
        val = val*(i+1)
    return val

list = [factorial(x) for x in range(11)]

print list

def reducep(x):
    array = []
    for i in range(9,0,-1):
        counter = 0
        while x+1 > factorial(i):
            x = x - factorial(i)
            counter += 1
        array.append(counter)
    return array

print reducep(3)

order = [0,1,2,3,4,5,6,7,8,9]
new = []

for x in reducep(999999):
    new.append(order.pop(x))
new.extend(order)

print new