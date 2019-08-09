from prime_functions import primes_up_to


def lcm(a,b):
    """ Finds the LCM of two integers a and b """

    a, b = min(a, b), max(a, b) # a <= b

    # Generate primes up to a
    primes = primes_up_to(a)

    lcm = 1

    while a != 1: # Until all prime factors of a are found
        for p in primes:
            while a % p == 0: # while p divides a
                lcm *= p
                a //= p
                if b % p == 0: # if p also divides b
                    b //= p

    # Now, lcm = a, and b has had all of its common factors with a removed

    lcm *= b
    return lcm


def LCM(x):
    """ Finds the LCM of a list of integers x """

    while len(x) != 1: # while x has multiple entries
        # Replace 2nd (#1) element with lcm of #0 and #1
        x[1] = lcm(x[0], x[1])
        # Remove first (#0) element
        x.pop(0)

    return x[0]


numbers = list(range(1, 21))
print(LCM(numbers))
