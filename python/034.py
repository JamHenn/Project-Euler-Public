def fac(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# store factorials in a list,
# so they only have to be calculated once
factorial = [] # 0!,...,9!
for i in range(10):
    factorial.append(fac(i))

nine = factorial[9] # 9!
n = 1 # maximum possible number of digits
# highest possible digit factorial sum with n+1 digits
# vs. lowest possible n+1 digit number
# 2nd quantity grows exponentially, 1st grows linearly
while ((n+1)*nine > 10**n):
    n += 1

# print(n, n*nine, 10**(n-1))
# numbers with the digit factorial property
# can have at most n=7 digits
list = []
for i in range(10, 10**n): # 2 to n digits
    digits = str(i)
    digitfac = 0
    for digit in digits:
        digitfac += factorial[int(digit)]
    if i == digitfac:
        list.append(i)

print(list)
print(sum(list))
