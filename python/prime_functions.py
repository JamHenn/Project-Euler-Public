import math # sqrt function

def primes_up_to(n):
    """Generates the prime numbers up to n>=2"""

    primes = [2]

    # check all odd numbers from 3 to n
    for i in range(3, n+1, 2):
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

    return primes


def largest_prime_factor(n):
    """ Finds the largest prime factor of the integer n """

    p = 2 # initial prime number
    primes = [p] # list of primes

    while n not in primes:
        # if p is a prime factor
        if n % p == 0:
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

    # The while loop breaks when n becomes prime.
    # Since the prime factors were divided out in
    # ascending order, n is now the largest prime factor.

    return n


def largest_prime_factor(n):
    """ Finds the largest prime factor of the integer n """

    for p in primes:
        # if p is a prime factor, divide it out
        while n % p == 0:
            n //= p
        if n in primes:
            break
        elif n == 1:
            n = p # p was the largest factor
    # The for loop breaks when n becomes prime.
    # Since the prime factors were divided out in
    # ascending order, n is now the largest prime factor.
    return n


def isprime(n):
    """ Tests if the integer n is prime """

    if n == 1:
        return False
    elif n < 4: # n = 2,3
        return True
    elif ((n % 2 == 0) or (n % 3 == 0)) : # 2 or 3 divides n
        return False
    elif n < 9: # n = 5,7
        return True
    else: # n = 6k +- 1 for k>=2.
        i = 5 # test if i divides n. 2 and 3 do not.
        sqrt = int(math.sqrt(n)) # floor of square root

        # Only primes below sqrt(n) need to be checked
        while i < sqrt+1:
            if n % i == 0:
                return False
            elif n % (i+2) == 0:
                return False
            i += 6
    return True


def prime_factorisation(n):
    """ Returns the prime factorisation of n in a dictionary """

    factors = {}

    p = 2 # p is the smallest potential prime factor of n
    while n % p == 0:
        # if p is not in the dictionary, add it with value 1
        # if p is in the dictionary, add 1 to its value
        factors[p] = factors.get(p, 0) + 1
        n //= p

    p = 3
    while n % p == 0:
        factors[p] = factors.get(p, 0) + 1
        n //= p

    p, i = 5, 0 # i=0,1 will be used to skip every 3rd odd number (not prime)
    while p**2 <= n: # if p^2 > n, then n has no more factors
        # p is the smallest potential factor, so if it is a factor,
        # it must be prime
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p

        p += 2 * (1 + i)
        i += 1
        i %= 2

    # the while loop breaks when n has no more factors smaller than itself
    # so n is either 1 or a prime number

    if n != 1:
        factors[n] = 1

    return factors


def sieve(limit):
    """
    Gives a sieve of composite odd numbers from 3 to limit

    (Input) limit: find composites/primes up to this number

    (Output) sieve: sieve[i] = True iff (2*i + 3) is composite
    """

    # number of odd numbers from 3 to limit
    sievebound = (limit - 1) // 2

    # 2i+3 is composite for i = 0,...,sievebound
    sieve = [False for i in range(sievebound)]

    # indices of potential composite numbers
    crosslimit = math.floor(math.sqrt(limit) - 1) // 2

    for i in range(crosslimit):
        if not sieve[i]: # ith odd number after 1 is prime
            # p = 2i + 3
            # p^2 = 4i^2 + 12i + 9 = 2(2i^2 + 6i + 3) + 3
            # p^2 is the (2i^2 + 6i + 3) odd number after 1
            for j in range(2*i**2 + 6*i + 3, sievebound, 2*i + 3):
            # j = p^2 to limit, step size p
                sieve[j] = True # composite because p divides 2j+3
