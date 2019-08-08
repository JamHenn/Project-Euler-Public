def sum_multiples(n, N):
    """
    Sums the multiples of n between 1 and N-1

    Input:
    n, N should be natural numbers, with n < N
    """

    # The number of summands
    num_terms = (N-1)//n

    return n * (num_terms * (num_terms + 1) / 2)

answer = sum_multiples(3, 1000) + sum_multiples(5,1000) - sum_multiples(15,1000)
print(answer)
