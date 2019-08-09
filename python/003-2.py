from prime_functions import primes_up_to

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


n = 10000
primes = primes_up_to(n)
print(largest_prime_factor(600851475143))
