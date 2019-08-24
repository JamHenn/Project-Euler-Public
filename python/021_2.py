from prime_functions import prime_factorisation

def d(n):
    """ Returns the sum of the proper divisors of n """

    multiplicands = []
    prime_factors = prime_factorisation(n)

    for p, k in prime_factors.items():
        i, multiplicand = 0, 0
        while i <= k:
            multiplicand += p ** i
            i += 1
        multiplicands.append(multiplicand)

    sum = 1 # sum of all factors
    for m in multiplicands:
        sum *= m

    # sum of proper factors
    return sum - n


n = 10000
sum = 0
for a in range(2, n):
    b = d(a)
    if a < b: # don't count each pair twice
        if d(b) == a: # a, b are an amicable pair
            sum += a + b

print(sum)
