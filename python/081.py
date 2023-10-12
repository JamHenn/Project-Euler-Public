def reduce_row(matrix, n):
    """
    Reduce the nth row
    n is a 1-based index
    Remove the n+1 row (if n is not the last row)
    """

    # If this is the last row
    if len(matrix) == n:
        for j in range(n-2, -1, -1):
            # Add the entry to the right
            matrix[n-1][j] += matrix[n-1][j+1]
        return

    for j in range(n-2, -1, -1):
        # Add the value below or to the right (whichever is smaller)
        matrix[n-1][j] += min(matrix[n][j], matrix[n-1][j+1])

    # n+1 row not needed anymore
    matrix.pop()


def reduce_column(matrix, n):
    """
    Reduce the nth column
    n is a 1-based index
    Remove the n+1 column (if n is not the last column)
    """

    # If n is the last column
    if len(matrix[0]) == n:
        for i in range(n-2, -1, -1):
            # Add the entry below
            matrix[i][n-1] += matrix[i+1][n-1]
        return

    for i in range(n-2, -1, -1):
        # Add the value below or to the right (whichever is smaller)
        matrix[i][n-1] += min(matrix[i+1][n-1], matrix[i][n])

    # n+1 column not needed anymore
    for row in matrix:
        row.pop()


def reduce_corner(matrix, n):
    """Reduce the nth row and the nth column (n is a 1-based index)"""

    # This part assumes the matrix is a square
    if n != len(matrix):
        matrix[n-1][n-1] += min(matrix[n][n-1], matrix[n-1][n])

    reduce_row(matrix, n)
    reduce_column(matrix, n)


def reduce_square_matrix(matrix):
    for n in range(len(matrix), 0, -1):
        reduce_corner(matrix, n)

    return matrix[0][0]


example_matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

print("\nFor the example matrix:\n")
for row in example_matrix:
    print(row)
print(f"\nThe minimal path sum is {reduce_square_matrix(example_matrix)}.")

with open('../data/p081_matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

print("\nFor the challenge matrix:")
print(f"The minimal path sum is {reduce_square_matrix(matrix)}.")
