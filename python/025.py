import math # sqrt

'''
F(n) ~ phi^n / sqrt(5)
phi^n / sqrt(5) > 10^(d-1)
n > (1/2 ln(5) + (d-1) ln(10)) / ln(phi)
'''

phi = (1.0 + math.sqrt(5)) / 2.0

d = 1000
bound = (math.log(5)/2.0 + (d-1)*math.log(10)) / math.log(phi)

print(bound)
print(int(bound) + 1)
