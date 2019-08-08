sum = 0

fib_num = 1
fib_num_copy = fib_num
next_fib_num = 2

while next_fib_num <= 4000000:
    # If the fibonacci number is even, include it in the sum.
    if next_fib_num % 2 == 0:
        sum += next_fib_num

    fib_num = next_fib_num
    next_fib_num += fib_num_copy
    fib_num_copy = fib_num

print(sum)
