from prime_functions import primes_up_to

# want to find all (4) a/b<1 (a<b) such that
# a/b = ac/bc, ac/cb, ca/bc or ca/cb for some c /=0
fractions = []
# a/b = ac/bc or ca/cb implies a=b (not valid)

# a/b = ac/cb implies c = 9ab/(10a-b)
# a/b = ca/bc implies c = 9ab/(10b-a)

for a in range(1, 10): # 1 to 9
    for b in range(a+1, 10): # a+1 to 9
        if (9*a*b % (10*a-b) == 0):
            if (9*a*b // (10*a-b)) < 10:
                fractions.append((a,b,9*a*b // (10*a-b),"ac/cb"))
        elif (9*a*b % (10*b-a) == 0):
            if (9*a*b // (10*b-a)) < 10:
                fractions.append((a,b,9*a*b // (10*b-a),"ca/bc"))

print(fractions)
top, bot = 1, 1
for i in range(4):
    top *= fractions[i][0]
    bot *= fractions[i][1]

# From problem 5

def lcm(a,b):
    """ Finds the LCM of two integers a and b """

    a, b = min(a, b), max(a, b) # a <= b

    # Generate primes up to a
    primes = primes_up_to(a)

    lcm = 1

    while a != 1: # Until all prime factors of a are found
        for p in primes:
            while a % p == 0: # while p divides a
                lcm *= p
                a //= p
                if b % p == 0: # if p also divides b
                    b //= p

    # Now, lcm = a, and b has had all of its common factors with a removed

    lcm *= b
    return lcm

def gcd(a,b):
    return (a * b) // lcm(a,b)

print(top, bot)
gcd = gcd(top, bot)
print(top // gcd, bot // gcd)
