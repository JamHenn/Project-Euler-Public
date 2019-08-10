with open('013.txt', 'r') as f:
    numbers = [int(line) for line in f]

sum = sum(numbers)
answer = str(sum)[:10] # first 10 digits of sum
print(answer)
