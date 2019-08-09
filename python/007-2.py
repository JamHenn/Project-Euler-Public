import math # sqrt function

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

i = 3
n = 10001
count = 1
while True:
    count += isprime(i)
    if count == n:
        print(i)
        break
    i += 2
