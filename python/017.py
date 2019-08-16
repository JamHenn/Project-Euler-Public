# one, two, ..., nine
units_letters = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
# twenty, thirty, ..., ninety
tens_letters = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
# ten, eleven, ..., nineteen
teens_letters = {0: 3, 1: 6, 2: 6, 3: 8, 4: 8, 5: 7, 6:7, 7: 9, 8: 8, 9: 8}


count = 0
# 1 to 9
count += sum(units_letters.values())
sum1 = count
# 10 to 19
count += sum(teens_letters.values())
sum2 = count
# 20 to 99
count += 10*sum(tens_letters.values()) + 8*sum(units_letters.values())
sum3 = count
# 100 to 999
count += sum1*100 + 9 * (7*100 + 3*99 + sum3)
# 1000
count += 3+8
print(count)
