def alt_fact(n):
    """ Computes n! with trailing zeros removed """

    result = 1
    '''
    # This doesnt deal with 25 = 5*5 correctly
    while n > 1:
        if n % 5 == 0:
            # divide out the factor of 5 and the factor
            # of 2 contributed by n and (n-1)
            # (one of them is even)
            factor = n * (n-1) // 10
            result *= factor
            n -= 2 # 2 steps
        else:
            result *= n
            n -= 1
    '''
    i = 2 # i increments from 2 to n
    j = i # at each step, we multiply by j
    while i <= n:
        while (j % 5 == 0):
            # divide out the factors of 5 contributed by i.
            # There are more numbers below i which are
            # divisible by 2 than divisible by 5, so we can
            # also divide out a factor of 2.
            j //= 5
            result //= 2

        result *= j
        i += 1
        j = i

    return result

n = 100
digits = str(alt_fact(n))
answer = sum([int(digit) for digit in digits])
print(answer)
