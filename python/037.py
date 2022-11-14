from prime_functions import isprime

def remove_digit(side, n):
    if side[0].lower() == 'l':
        return int(str(n)[1:])
    elif side[0].lower() == 'r':
        return int(str(n)[:-1])

    raise Exception('Invalid direction. Should be \'left\' or \'right\'.')


def is_truncatable_prime(direction, n):
    if n < 10: # 1 digit
        return n in [2, 3, 5, 7]

    if isprime(n):
        truncated_number = remove_digit(direction, n)
        return is_truncatable_prime(direction, truncated_number)

    return False


def truncatable_prime(n):
    return is_truncatable_prime('left', n) and is_truncatable_prime('right', n)


number_truncatable_primes = 11
truncatable_primes_found = 0
sum = 0

# Not counting 1-digit primes
# Primes above 10 have the form: 6k +- 1 for k>=2
number = 11
i = 0 # i=0,1 is used to skip every 3rd odd number

print("The truncatable primes are:")
while truncatable_primes_found < number_truncatable_primes:
    if truncatable_prime(number):
        print(number)
        truncatable_primes_found += 1
        sum += number
    number += 2 * (1+i)
    i += 1
    i %= 2

print(f"\nTheir sum is {sum}.")
