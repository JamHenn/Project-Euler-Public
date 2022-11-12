from prime_functions import prime_factorisation, prime_factorisation_string

def distinct_prime_factors(n):
    prime_factor_dict = prime_factorisation(n)

    return list(prime_factor_dict.keys())

def first_consec_nums_with_prime_factors(consecutive_length, num_prime_factors):
    n = 2 # start of consecutive numbers

    while True:
        result_found = True
        # consecutive number list
        consec_nums = list(range(n, n+consecutive_length))
        for number in consec_nums:
            if len(distinct_prime_factors(number)) < num_prime_factors:
                result_found = False
                break

        if result_found:
            return consec_nums

        n += 1

def print_results(consecutive_length, num_prime_factors):
    print(f"\nThe first {consecutive_length} consecutive numbers to have {num_prime_factors} distinct prime factors are:")

    answer = first_consec_nums_with_prime_factors(consecutive_length, num_prime_factors)
    for number in answer:
        factorisation_string = prime_factorisation_string(number)
        print(f"{number} = {factorisation_string}")

print_results(2,2)
print_results(3,3)
print_results(4,4)
