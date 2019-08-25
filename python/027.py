from prime_functions import isprime, sieve


def quadratic(n, a, b):
    return n**2 + a*n + b


limit = 1000
if limit % 2 == 0: # limit is even
    limit -= 1

sieve = sieve(limit) # sieve[i] = True iff (2*i + 3) is composite

max = 0 # the maximum number of consecutive primes
amax, bmax = 0, 0 # the values of a and b which give the most primes
#for all b
for i, bool in enumerate(sieve):
    if bool: # 2i+3 is composite
        continue
    else: # 2i+3 is prime
        b = 2*i + 3

    for a in range(-limit, limit + 1, 2): # a is odd
        n = 1 # n = 0 gives a prime
        while isprime(quadratic(n, a, b)):
            n += 1
        # n is the number of consecutive primes
        if n > max:
            max, amax, bmax = n, a, b

print("n^2 + an + b is prime for n = 0, 1, ..., {}\n when (a, b) = ({}, {})".format(max-1, amax, bmax))
print("ab =" + str(amax * bmax))
