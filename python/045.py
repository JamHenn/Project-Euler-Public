overlap = 0 # number of times the three sequences are equal
i, j = 1, 1
H, P = 1, 1 # the first hexagonal and pentagonal numbers
while overlap < 3:
    while H != P:
        if H > P:
            P += (3*j + 1) # P_(j+1)
            j += 1
        else: # H < P
            H += (4*i + 1) # H_(i+1)
            i += 1
    overlap += 1
    print(i, H, j, P)
    
    # Find next numbers in the sequences
    P += (3*j + 1) # P_(j+1)
    j += 1
    H += (4*i + 1) # H_(i+1)
    i += 1
