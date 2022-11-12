import math

def cubes_of_length(digits):
    # Smallest d-digit number: 10^(d-1)
    # Take cube root, and then take ceiling
    lower_base = math.ceil(math.pow(10, (digits-1.0)/3.0))

    # Largest d-digit number: 10^d - 1
    # Take cube root, and then take ceiling
    upper_base = math.floor(math.pow(10.0**digits - 1.0, 1.0/3.0))

    return [x**3 for x in range(lower_base, upper_base+1)]


def is_permutation(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


def cube_permutation_dict(digits):
    cubes = cubes_of_length(digits)

    # Count permutations. Every cube has one (itself).
    # Only the smallest in a tuple of permutations will have the full count.
    permutation_dict = {cube:1 for cube in cubes}
    for index, cube in enumerate(cubes):
        for bigger_cube in cubes[index+1:]:
            permutation_dict[cube] += is_permutation(cube, bigger_cube)

    return permutation_dict


def smallest_cube_with_permutations(n):
    digits = 0
    while True:
        cube_permutations = cube_permutation_dict(digits).items()
        for cube, permutation_count in cube_permutations:
            if permutation_count == n:
                return cube

        digits += 1


def print_results(permutation_count):
    smallest_cube = smallest_cube_with_permutations(permutation_count)
    print(f"The smallest cube which can be permuted to produce {permutation_count} cubes is {smallest_cube}")


for i in range(1, 6):
    print_results(i)
