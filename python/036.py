def palindrome():
    """ Generates palindromes less than 1 million """

    i = 1
    while i < 10:
        yield i
        i += 1

    i = 1
    while i < 10:
        yield int(str(i) * 2)
        i += 1

    while i < 100:
        yield int(str(i) + str(i)[0])
        i += 1

    i = 10
    while i < 100:
        yield int(str(i) + str(i)[::-1])
        i += 1

    while i < 999:
        yield int(str(i) + str(i)[:2][::-1])
        i += 1

    i = 100
    while i < 999:
        yield int(str(i) + str(i)[::-1])
        i += 1

'''
for i in palindrome():
    print(i)'''

def base_2(n):
    """ Convert n to base 2 """

    if n == 0:
        return '0'

    ones = []
    while n != 0:
        i = -1
        p = 1
        # find highest power of 2 <= n
        while p <= n:
            p *= 2
            i += 1
        # stops when i is the highest power of 2 <= n
        # and p is twice the highest power
        p //= 2
        ones.append(i)
        n -= p

    binary = ''
    for i in range(ones[0], -1, -1): # highest power to 1
        if i in ones:
            binary += '1'
        else:
            binary += '0'

    return binary


sum = 0
for palindrome in palindrome():
    if (palindrome % 2) == 0:
        continue # only odd numbers can be palindromes in base 2
    else:
        binary = base_2(palindrome)
        sum += palindrome * (binary == binary[::-1])

print(sum)
# consider 1 digit palindromes
for i in range(10):
    print(base_2(i))
