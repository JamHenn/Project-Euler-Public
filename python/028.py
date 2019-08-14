def diag_spiral_sum(n):
    """ Returns the sum of the diagonals in a spiral on an n*n grid """
    # n must be odd

    return (4*n**3 + 3*n**2 + 8*n - 9) // 6


print(diag_spiral_sum(1001))    
