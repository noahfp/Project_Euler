import math

def power_digits(n, d):
    return [i**n for i in range(int(math.ceil(math.pow(10,(d-1)/float(n)))), int(math.ceil(math.pow(10,d/float(n)))))]

# testing gives 9^21 largest power which is still 21 digits long. 

print sum([len(power_digits(n,n)) for n in range(1, 22)])
