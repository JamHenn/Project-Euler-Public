import itertools

def lexicographic_permutations(ls):
    # Ensure lexicographic order when permuted
    ls = list(ls)
    ls.sort()

    return itertools.permutations(ls)

# 1 millionth permutation of 0-9
solution = list(lexicographic_permutations(range(10)))[1000000-1]
solution_string = ''.join([str(element) for element in solution])
print(solution_string)
