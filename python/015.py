def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def C(n,k):
    """ Computes n choose k for k<=n """

    return factorial(n) // (factorial(k) * factorial(n-k))

# grid dimensions
I, J = 20, 20
# I+J total steps: choose I left steps
print(C(I+J, I))
