from prime_functions import sieve

limit = 1000000 - 1
sieve = sieve(limit)


def is_cp(p):
    """ Tests whether a given prime number is circular """

    if p == 2: # 2 is not in the sieve
        return True

    if '0' in str(p): # 101 -> 11 -> 11  infinite loop
        return False

    conjugate = int(str(p)[1:] + str(p)[0])

    if conjugate % 2 == 0: # conjugate is even
        return False
    j = (conjugate - 3) // 2 # sieve index. Only valid for odd conjugate
    if sieve[j]: # conjugate is composite
        return False

    while conjugate != p:
        conjugate = int(str(conjugate)[1:] + str(conjugate)[0])

        if conjugate % 2 == 0: # conjugate is even
            return False
        j = (conjugate - 3) // 2 # sieve index. Only valid for odd conjugate
        if sieve[j]: # conjugate is composite
            return False

    return True


# check primes in asending order
count = is_cp(2)
for i in range(len(sieve)):
    if not sieve[i]: # 2i+3 is prime
        p = 2*i + 3
        count += is_cp(p)
                    
print(count)
