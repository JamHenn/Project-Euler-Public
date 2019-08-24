import math # sqrt

def d(n):
    """ Returns the sum of the proper divisors of n """

    if n == 1:
        return 0

    if n % 2 == 0: # n even
        start = 2; step = 1
    else: # odd numbers only have odd factors
        start = 3; step = 2

    stop = int(math.sqrt(n))
    if stop ** 2 == n: # n is a square
        sum = 1 + stop
    else:
        sum = 1 # 1 is a proper divisor, n is not

    for i in range(start, stop, step):
        if n % i == 0: # i is a divisor
            sum += i + n//i
            if i * i == n: # i = sqrt(n)
                sum -= i

    return sum


n = 10000
sum = 0
for a in range(2, n):
    b = d(a)
    if a < b: # don't count each pair twice
        if d(b) == a: # a, b are an amicable pair
            sum += a + b

print(sum)
