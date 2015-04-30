largest = 1

def collatz(x):
    global largest
    if x%2 == 0:
        return x/2
    else:
        largest = max(largest,3*x+1)
        return 3*x+1

arr = [0,0]

def check(x,v):
    global arr
    if x > v-1:
        return check(collatz(x),v) + 1
    else:
        return arr[x]


cap = 1000000

for i in range(2,cap):
    arr.append(check(i,i))

mx = 0
val = 1

for i in range(cap):
    if arr[i] > mx:
        mx = arr[i]
        val = i

print val
print largest
