for a in range(1, 334):
    if ((1000 * (a - 500)) % (a - 1000)) == 0:
        b = (1000 * (a - 500)) // (a - 1000)
        c = 1000 - a - b
        print(a * b * c)
        break
