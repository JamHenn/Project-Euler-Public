import math # Need sqrt and ceil functions

def is_product(n, d):
    """ Tests whether the integer n is a product of two d-digit numbers """

    largest = 10**d -1 # largest d-digit number
    smallest = 10**(d-1) # smallest d-digit number

    sqrt = math.ceil(math.sqrt(n))

    answer = False

    for i in range(largest, sqrt-1, -1):
        if ((n % i == 0) and (smallest <= (n // i) <= largest)):
            answer = True
            break

    return answer


def palindrome(n):
    """ Converts n into a palindrome e.g. ABC -> ABCCBA """

    digits = [] # This will store the digits of n
    palindrome = 0

    while n != 0:
        digits.append(n % 10) # last digit
        n -= digits[-1] # change last digit to 0
        n //= 10 # remove the zero from the end

    digits.reverse() # The digits are currently stored in reverse order
    d = len(digits) # number of digits of n

    for i, digit in enumerate(digits):
        palindrome += digit * (10 ** (2*d - (i+1)) + 10 ** i)

    return palindrome


d = 3
largest = 10**d -1 # largest d-digit number
smallest = 10**(d-1) # smallest d-digit number

# Test 2d-digit palindromes in decreasing order
for i in range(largest, smallest-1, -1):
    if is_product(palindrome(i), d):
        print(palindrome(i))
        break
