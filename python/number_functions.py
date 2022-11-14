def is_permutation(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


def ordered_permutation(number):
    """Returns digits in descending order. This removes the problem of leading zeros"""
    ordered_digits = sorted(str(number), reverse=True)

    return int(''.join(ordered_digits))


def count_permutations(num_list):
    """Returns key-value pairs: (N, #permutations of N in num_list)"""

    permutation_dict = {number:1 for number in num_list}
    for index, number in enumerate(num_list):
        for number2 in num_list[index+1:]:
            if is_permutation(number, number2):
                permutation_dict[number] += 1
                permutation_dict[number2] += 1

    return permutation_dict


def permutation_list(num_list):
    """
    Returns a list of lists of permutations within num_list.

    Duplicates in num_list will not show up twice in the result.
    """

    permutation_dict = {}
    for index, number in enumerate(num_list):
        for number2 in num_list[index+1:]:
            if is_permutation(number, number2):
                # Group numbers by their sorted permutation
                key = ordered_permutation(number)

                # Add first number if the value is empty
                if permutation_dict.get(key) is None:
                    permutation_dict[key] = [number]

                # Add second number
                if number2 not in permutation_dict[key]:
                    permutation_dict[key].append(number2)

    return list(permutation_dict.values())
