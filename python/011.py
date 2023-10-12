with open('data/011.txt', 'r') as f:
    data = [[int(num) for num in line.split(' ')] for line in f]


def max_prod(X, n):
    """ Finds the largest product of n adjacent numbers """

    I, J = len(X), len(X[0]) # dimensions
    max_prod = 0

    # horizontal products
    for i in range(I):
        for j in range(J-n+1): # entries 0 to J-n. Start of product.
            prod = 1
            for k in range(n): # k = 0,1,...,(n-1)
                prod *= X[i][j+k]
            if prod > max_prod:
                max_prod = prod
                start = (i, j)
                end = (i, j+n-1)

    # vertical products
    for j in range(J):
        for i in range(I-n+1): # (0,j) to (I-n, j). Start of product.
            prod = 1
            for k in range(n): # k = 0,1,...,(n-1)
                prod *= X[i+k][j]
            if prod > max_prod:
                max_prod = prod
                start = (i, j)
                end = (i-n+1, j)

    # main diagonals
    # Start in upper (I-n+1)x(J-n+1) submatrix
    for i in range(I-n+1): # i = 0,1,...,(I-n)
        for j in range(J-n+1): # j = 0,1,...,(I-n)
            prod = 1
            for k in range(n): # k = 0,1,...,(n-1)
                prod *= X[i+k][j+k]
            if prod > max_prod:
                max_prod = prod
                start = (i, j)
                end = (i+n-1, j+n-1)

    # secondary diagonals
    # Start in lower (I-n+1)x(J-n+1) submatrix
    for i in range(n-1, I): # i = (n-1),n,...,(I-1)
        for j in range(J-n+1): # j = 0,1,...,(J-n)
            prod = 1
            for k in range(n): # k = 0,1,...,(n-1)
                prod *= X[i-k][j+k]
            if prod > max_prod:
                max_prod = prod
                start = (i, j)
                end = (i-n+1, j+n-1)

    return max_prod, start, end

print(max_prod(data, 4)[0])
# print(data[15][3], data[14][4], data[13][5], data[12][6])
# print(data[15][3] * data[14][4] * data[13][5] * data[12][6])
