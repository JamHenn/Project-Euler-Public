import math # for sqrt function

def primes_up_to(n):
    """ Generates the prime numbers up to integer n>=2 """

    primes = [2]

    # check all odd numbers from 3 to n
    for i in range(3, n+1, 2):
        for p in primes:
            if i % p == 0: # i composite
                break
            # If all primes have been checked, then i is prime.
            elif p == primes[-1]:
                primes.append(i)

    return primes


def prime_factors(n):
    """ Finds the prime factors of the integer n>=4 """

    # List of primes up to sqrt(n)
    primes = primes_up_to( round(math.sqrt(n)) )

    prime_factors = []

    # If n is not known to be prime, then find a prime factor.
    while n not in primes:
        for p in primes:
            # If p divides n, it is a factor.
            if n % p == 0:
                prime_factors.append(p)
                n //= p
                break
        # If all primes in the list have been checked,
        # then what remains of n must be a prime
        else:
            # break out of the while loop
            break

    # The while loop breaks iff n is prime
    prime_factors.append(n)

    return sorted(prime_factors)

# print(math.sqrt(600851475143))

# Generating primes_up_to(775,146) takes too long
