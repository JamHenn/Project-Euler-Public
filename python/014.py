def collatz_length(n):
    """ Computes the length of the Collatz sequence starting at n """

    length = 1 # include n, the first term

    while n != 1:
        if n % 2 == 0: # if n is even
            n //= 2
            length += 1 # new term has been generated
        else: # if n is odd
            n = (3 * n + 1) // 2
            length += 2 # 2 steps

    return(length)


max_length = 1
answer = 1
# numbers below 500000 cannot have the longest sequence
# if i<500000 then 2i<1000000 has a longer sequence
for i in range(500000, 1000000):
    # if (i + 2) = 6k, then i = 3*(2k-1)+1
    # i = 3*m+1, m odd, m<i<1000000; so m has a longer sequence
    if (i + 2) % 6 == 0:
        continue
    else:
        length = collatz_length(i)
        if length >= max_length:
            answer = i
            max_length = length

print(answer)
