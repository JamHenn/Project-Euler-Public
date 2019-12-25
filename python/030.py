"""
a1a2..an vs a1^k+..+an^k
LHS grows exponentially with n
RHS grows linearly with n
LHS will eventually be bigger
So: Stop looking once the smallest possible LHS
exceeds the largest possible RHS
"""
k = 5 # power
d = 2 # number of digits
# Can n*9^k have n digits?
while len(str(((d+1)*9**k))) >= d+1:
    d += 1
    print(d, d*9**k)
# a number which has the digit power property has at most d digits

list = []
# 2 digits - highest powersum for a d-digit-number
for i in range(10, d*9**k+1):
    digits = str(i)
    powsum = 0
    for digit in digits:
        powsum += int(digit)**k
    if i == powsum:
        list.append(i)

print(list)
print(sum(list))
