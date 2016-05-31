def factorial(x):
    val = 1
    for i in range(x):
        val = val*(i+1)
    return val

s = str(factorial(100))
total = 0
for c in s:
    total += int(c)
print total