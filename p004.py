def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

def large_palindrome(cap):
    for i in range(cap):
        for j in range(i):
            val = (cap-j)*(cap-i+j)
            if is_palindrome(val):
                return val
    return -1

print large_palindrome(int(raw_input("")))


