def largest_prime_factor(n):
    """ Finds the largest prime factor of the integer n """

    p = 2 # initial prime number
    primes = [p] # list of primes
    max_prime_factor = p

    while n not in primes:
        # if p is a prime factor
        if n % p == 0:
            max_prime_factor = max(max_prime_factor, p)
            # divide the factor p out of n
            n //= p
            while n % p == 0:
                n //= p

        # if p is not a prime factor, find the next prime number
        elif p == 2:
            p += 1
            primes.append(p)

        else:
            while True:
                p += 2 # next odd number
                # Only need to consider primes up to sqrt(p)
                potential_factors = [x for x in primes if x**2 <= p]
                for prime in potential_factors:
                    if p % prime == 0: # if p is composite
                        break # move to next odd number
                # If no primes up to sqrt(p) are factors, then p is prime
                else:
                    primes.append(p)
                    break # break out of the while loop

    # The while loop breaks when n becomes prime
    max_prime_factor = max(max_prime_factor, n)

    return max_prime_factor

print(largest_prime_factor(600851475143))
