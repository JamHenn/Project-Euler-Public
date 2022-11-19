def satisfies_goldbach(n, primes):
    """Try to find a prime of the form n-2a^2 primes"""
    a = 1
    while n - 2*a**2 >= 2:
        if n - 2*a**2 in primes:
            print(f"{n} = {n - 2*a**2} + 2*{a}^2")
            return True
        a += 1
    return False


def is_prime(n, primes):
    for p in primes:
        if n % p == 0: return False
    return True


# Note: primes will contain all prime numbers up to n
# This is all that is needed for the functions above
primes = [2]
n = 1
while True:
    # Next odd number
    n += 2
    if is_prime(n, primes):
        primes.append(n)
        continue

    if satisfies_goldbach(n, primes):
        continue

    # Break when n is a composite number which doesn't satisfy the conjecture
    break

print(f"\nThe smallest odd, composite number which does not satisfy the Goldbach criterion is {n}.")
