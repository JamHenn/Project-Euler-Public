def prime(n):
    """ Finds the nth prime number """

    primes = [2]
    i = 1 # Start by checking i=3

    while len(primes) < n:
        i += 2
        # Only need to check primes up to sqrt(i)
        if i != 3:
            potential_prime_factors = [x for x in primes if x**2 <= i]
        # There are no primes below sqrt(3)
        else:
            potential_prime_factors = [2]


        for p in potential_prime_factors:
            if i % p == 0: # i composite
                break
        # If all primes have been checked, then i is prime.
        else:
            primes.append(i)

    return primes[-1]


print(prime(10001))
