def sum_square_diff(n):
    return ((n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6)

print sum_square_diff(int(raw_input("")))