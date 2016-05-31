from math import log10 

n = 4770
while n*log10(((5**0.5+1)/2)) - log10(5**0.5) < 999:
    n += 1

print n