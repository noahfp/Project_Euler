def factorial(x):
    val = 1
    for i in range(x):
        val = val*(i+1)
    return val

print factorial(40)/(factorial(20)*factorial(20))