def cap_n_primes(n):
    primes = [2]
    num = 3
    counter = 1
    while num < n:
        fault = 0
        for p in primes:
            if p > int(num**0.5)+1:
                break
            if num % p == 0:
                fault = 1
                break
        if fault == 0:
            primes.append(num)
            counter += 1
        num += 2
    return primes

print sum(cap_n_primes(2000000))