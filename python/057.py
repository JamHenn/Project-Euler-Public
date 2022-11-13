"""
sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))

Sequence:
a_1 = 1 + 1/2
a_2 = 1 + 1/(2+1/2)
a_3 = 1 + 1/(2+1/(2+1/2))
...

Can see the following recursion:
a_(n+1) = 1 + 1/(1 + a_n)
"""
from fractions import Fraction

def recursive_step(a):
    return 1 + Fraction(1, 1 + a)


def iteration(n):
    current_term = Fraction(3,2)
    for _ in range(n):
        yield current_term
        current_term = recursive_step(current_term)


def is_numerator_longer_than_denominator(fraction):
    return len(str(fraction.numerator)) > len(str(fraction.denominator))


number_of_terms = 1000
count = 0
for term in iteration(number_of_terms):
    count += is_numerator_longer_than_denominator(term)

print(f"In the first {number_of_terms} expansions, {count} fractions have more digits in their numerator.")
