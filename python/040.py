"""
Consider the sequence 1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,...
Made by taking the digits of the natural numbers in order.

To solve Problem 40, we need a formula
to find the nth term in this sequence.

Note: This problem uses 1-based indexing.

---

d-digit numbers: [10^(d-1), 10^d - 1]
Note: This excludes 0 when d=1. Not needed for this problem.

Number of d-digit numbers:
= (upper bound) - (lower bound) + 1
= (10^d - 1) - 10^(d-1) + 1
= 10^d - 10^(d-1)
= 9 * 10^(d-1)

---

Number of 1-digit numbers: 9 * 10^0 = 9
Length of 1-digit numbers in sequence: 1 * 9

Number of 2-digit numbers: 9 * 10^1 = 90
Length of 2-digit numbers in sequence: 2 * 90

Length of d-digit numbers in sequence: d * 9 * 10^(d-1)

---

Index of first (d+1) digit number in sequence:
First(d+1)
:= 1 + sum (n=1 to d) 9n * 10^(n-1)
 = 1 + 9/10 * sum (n=1 to d) n * 10^n

---

sum (n=1 to d) n * 10^n

Write this as:
sum (n=1 to d) sum (k=1 to n) 10^n

i.e.
10
+ 100 + 100
+ 1000 + 1000 + 1000
+ 10000 + 10000 + 10000 + 10000
...

Inner sum is each row.
Outer sum is the column vector after rows are added up.

Swap the order of summation:
Inner sum is each column.
Outer sum is the row vector after columns has been added up.

sum (k=1 to d) sum (n=k to d) 10^n

This can be computed in a few steps
using the geometric series formula.

Result:
10/81 (9d*10^d - 10^d + 1)

---

Back to the index of the first (d+1) digit number in the sequence:

First(d+1)
 = 1 + 9/10 * sum (n=1 to d) n * 10^n
 = 1 + 9/10 * 10/81 * (9d*10^d - 10^d + 1)
 = 1 + 1/9 * (9d*10^d - 10^d + 1)
 = d*10^d - (10^d-1)/9 + 1

First(d)
 = (d-1)*10^(d-1) - (10^(d-1)-1)/9 + 1

---

Consider the nth d-digit number:

What is this number?
Value(n, d) = 10^(d-1) + (n-1)

Where does it start in the sequence?
Index(n, d) = First(d) + (n-1)*d

For example, the 3rd 2-digit number:
Value(3, 2) = 10^(2-1) + (3-1) = 12
Index(3, 2) = First(2) + (3-1)*2
            = (2-1)*10^(2-1) - (10^(2-1)-1)/9 + 1 + 4
            = 10 - 1 + 1 + 4
            = 14

And the '1' in '12' is at the 14th index


---

Now, working backwards,
how do we find the nth term of the sequence?

1. Find the largest d such that First(d) <= n.
     This means that n is part of a d-digit number.
2. Compute k := (n-First(d))//d + 1.
     How far is n from First(d) in multiples of d?
     Call this number k-1.
     This means that the nth term is part of the
     kth d-digit number.
3. Compute Value(k, d).
     This is the kth d-digit number
4. Compute Index(k, d).
     This is the starting index of the kth d-digit number.
5. Compute n - Index(k, d).
     This is the index of the nth term within the number.
6. Find the nth term using the value of the number,
   and the index within that number.
"""

def first(d):
    """
    Returns the index of the first d-digit number in the sequence

    Formula:
    (d-1)*10^(d-1) - (10^(d-1)-1)/9 + 1

    Could compute first and second terms with strings
    for enhanced performance
    """
    return (d-1)*10**(d-1) - (10**(d-1)-1)//9 + 1


def value(n, d):
    """Returns the nth d-digit number"""
    return 10**(d-1) + (n-1)


def index(n, d):
    """
    Returns the starting index of the
    nth d-digit number in the sequence
    """
    return  first(d) + (n-1)*d


def digits_in_num_at_index(n):
    """
    Returns the number of digits in the number that
    the nth term is a part of.

    i.e. Finds the largest d such that first(d) < n
    """
    d = 1
    while first(d) <= n:
        d += 1

    # Loop breaks when first(d) > n
    return d - 1


def nth_term_in_sequence(n):
    """Returns the nth term in the sequence"""

    d = digits_in_num_at_index(n)

    # n is the kth d-digit number
    k = (n - first(d))//d + 1

    # number that nth term is part of
    number = str(value(k, d))

    # starting index of number
    starting_index = index(k, d)

    return int(number[n - starting_index])


product = 1
for n in [10**i for i in range(7)]:
    product *= nth_term_in_sequence(n)

print(product)
