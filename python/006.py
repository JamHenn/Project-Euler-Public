def sum(a, b):
    """ Adds the numbers from a to b inclusive """

    a, b = min(a, b), max(a, b) # a <= b

    sum1 = (b * (b + 1) // 2) # 1+2+...+b
    sum2 = (a * (a - 1) // 2) # 1+...+(a-1)

    return (sum1 - sum2)

def sum_sq(a, b):
    """ Adds the squares of the numbers from a to b inclusive """

    a, b = min(a, b), max(a, b) # a <= b

    sum1 = (b * (b + 1) * (2*b + 1) // 6) # 1^2+2^2+...+b^2
    sum2 = (a * (a - 1) * (2*a - 1) // 6) # 1^2+...+(a-1)^2

    return (sum1 - sum2)

answer = sum(1, 100)**2 - sum_sq(1, 100)
print(answer)
