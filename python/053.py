def min_binomial(N):
    """ Finds the minimal integer n such that nCk > N for some k """

    # First, find the minimal even n
    k, C = 1, 2 # k=1, C is 2k choose k
    while C < N:
        # convert [2k choose k] to [2(k+1) choose (k+1)]
        C *= (4*k + 2)
        C //= k + 1
        k += 1

    # 2k choose k = 2 * [(2k-1) choose k]
    if C > 2*N:
        n = 2*k - 1 # the minimal n is odd
    else:
        n = 2*k # the minimal n is even

    return n


def count_binomial(n, N):
    """ Counts the number of binomal coefficients nCk > N """

    k, C = 0, 1 # C = n choose k

    while C <= N:
        # convert [n choose k] to [n choose (k+1)]
        C *= n - k
        C //= k + 1
        k += 1

        if 2*k > n: # if the maximum binomial coefficient has been calculated
            return (C > N) # 0 or 1

    # Now, we have the minimum value of k st nCk > N
    # nCk, nC(k+1), ..., nC(n-k) > N
    return (n - 2*k + 1)


N = 1000000
max = 100
min = min_binomial(N) # min = 23 for N = 10^6
count = 0

for n in range(min, max+1):
    count += count_binomial(n, N)

print(count)
