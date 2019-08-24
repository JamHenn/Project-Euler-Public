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


i, triangle, max, max_triangle = 0, 0, 0, 0
while max < 500:
    i += 1
    triangle += i

    factors = prime_factorisation(triangle)
    n_factors = 1 # total number of divisors
    for number in factors.values():
        n_factors *= number + 1

    if n_factors > max:
        max = n_factors
        max_triangle = triangle
print(max, max_triangle)
