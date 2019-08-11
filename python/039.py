def num_py_trip(p):
    """ Counts the number of Pythagorean triples with sum p """

    count = 0
    if p % 2 == 1:
        return count

    for a in range(3, p//3): # 3 <= a <= (p-3)/3
        # is b an integer?
        b_int = (((p**2 - 2*a*p) % (2*(p - a))) == 0)
        count += b_int

    return count

max = 0
# any triple with p<501 can be doubled
for p in range(502, 1001, 2): # p must be even
    n = num_py_trip(p)
    if n > max:
        P, max = p, n

print(P, max)
