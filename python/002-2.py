# Need pow(,) and sqrt() functions
import math

def fib(n):
    """ Returns nth Fibonacci number """

    phi = (1 + math.sqrt(5)) / 2.0 # golden ratio
    psi = (1 - math.sqrt(5)) / 2.0 # golden ratio conjugate/inverse

    return round( (math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5) )

sum = 0

# The 3rd (0-based indexing) Fibonacci number, 2, is the first even one.
n = 3
fib_num = fib(n)

while fib_num <= 4000000:
    sum += fib_num

    # Every 3rd Fibonacci number is even.
    n += 3
    fib_num = fib(n)

print(sum)       
