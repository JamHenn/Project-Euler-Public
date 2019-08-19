def div(a, b):
    """ Gives the decimal expansion of a/b for a<b """

    expansion = []
    numerators = []
    repeating = True

    while True:
        a *= 10 # next decimal point

        if a in numerators:
            i = numerators.index(a) # location of first repeating digit
            expansion, rep_expantion = expansion[:i], expansion[i:]
            break
        else:
            numerators.append(a)

        expansion.append(a//b) # next digit
        a %= b # remainder after dividing by b
        if a == 0: # if b divides a
            repeating = False
            break

    if repeating:
        return "repeating", expansion, rep_expantion
    else:
        return expansion


max = 0
n = 1000
for i in range(2, n):
    x = div(1, i)
    if x[0] == 'repeating':
        if len(x[2]) > max:
            d, max = i, len(x[2])

print(d, max)
