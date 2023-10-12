with open("../data/022.txt", 'r') as f:
    names = sorted([name.strip('"') for name in f.read().split(',')])

total = 0
for i, name in enumerate(names):
    name_value = sum((ord(letter) - 64) for letter in name)
    name_score = (i + 1) * name_value
    total += name_score

print(total)
