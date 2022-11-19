from prime_functions import sieve, prime_sieve_up_to, primes_up_to

prime_limit = 10**6
primes = prime_sieve_up_to(prime_limit)

# Add the first (smallest) primes until the total exceeds the prime limit
# This gives an upper bound on the number of summands
max_terms, min_sum = 0, 0
while min_sum < prime_limit:
    min_sum += primes[max_terms]
    max_terms += 1
max_terms -= 1


def find_sum_of_length(n):
    # n is even => 2 is in the sum (sum must be odd)
    if n % 2 == 0:
        if sum(primes[:n]) in primes:
            return primes[:n]
    # n is odd => 2 is not in the sum
    else:
        for i in range(1, max_terms-n+1):
            if sum(primes[i:i+n]) in primes:
                return primes[i:i+n]


max_sum_length = max_terms
while True:
    summands = find_sum_of_length(max_sum_length)
    if summands is not None:
        print(f"A prime below {prime_limit} which can be written as the sum of the most consecutive primes is {sum(summands)}. The sum contains {len(summands)} terms.")
        break
    max_sum_length -= 1
