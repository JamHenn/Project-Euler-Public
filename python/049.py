from number_functions import ordered_permutation, permutation_list
from prime_functions import primes_up_to

def primes_of_length(d):
    # 10^d has d+1 digits.
    # 10^d - 1 is divisible by 9, and 10^d - 2 is even
    primes = primes_up_to(10**d - 3)

    for index, prime in enumerate(primes):
        if len(str(prime)) == d:
            return primes[index:]


def find_aritmetic_sequences(ordered_num_list):
    """Finds arithmetic sequence of length 3 in the ordered list"""

    sequences_of_length_3 = []
    for index, number in enumerate(ordered_num_list):
        for number2 in ordered_num_list[index+1:]:
            difference = number2 - number
            number3 = number2 + difference
            if number3 in ordered_num_list:
                sequences_of_length_3.append([number, number2, number3])

    return sequences_of_length_3


primes = primes_of_length(4)
prime_permutations = permutation_list(primes)
prime_permutations = [perm_list for perm_list in prime_permutations if len(perm_list) >= 3]

for permutations in prime_permutations:
    for sequence in find_aritmetic_sequences(permutations):
        print(sequence)
