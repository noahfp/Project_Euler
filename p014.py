# Hi Timmeh :3


# I only put 'largest' in my code because I was curious
# how big the numbers might get before going back to 1

largest = 1

# 'collatz' just checks even/odd then performs the appropriate 
# Collatz operation. You can ignore the 'largest' line.

def collatz(x):
    global largest
    if x%2 == 0:
        return x/2
    else:
        largest = max(largest,3*x+1)
        return 3*x+1


# 'arr' stores the number of steps required to get from i to 
# 1 in 'arr[i]'. I'll just define 0 and 1 to take (0) moves.

arr = [0,0]

# 'check' essentially iterates 'collatz' on x, but there's a heuristic
# I assume we are checking numbers starting from 2 and going up. This way
# if I call 'check(i,i)', if I ever get get to a value less than 'i', I 
# know that I've already calculated how many steps the rest of the time 
# takes, so just add on that value. This actually makes computation time
# exponentially faster.

def check(x,v):
    global arr
    if x > v-1:
        return check(collatz(x),v) + 1
    else:
        return arr[x]


cap = 1000000

# fill in all values of our array

for i in range(2,cap):
    arr.append(check(i,i))

# now find the value with the maximum number and report its array position

mx = 0
val = 1

for i in range(cap):
    if arr[i] > mx:
        mx = arr[i]
        val = i

print val
print largest
