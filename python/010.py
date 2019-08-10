from prime_functions import isprime

def prime_generator(limit):
    i = 2
    if i < limit: # i = 2
        yield i
        i += 1
    while i < limit:
        if isprime(i):
            yield i
        i += 2

sum = 0
limit = 2000000
for prime in prime_generator(limit):
    sum += prime
print(sum)
