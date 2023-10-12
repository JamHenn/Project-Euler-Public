with open("data/067.txt", 'r') as f:
    triangles = [[int(num) for num in line.split()] for line in f]

I = len(triangles)
for i in range(I-2, -1, -1): # 2nd last row to 1st row
    for j in range(len(triangles[i])):
        triangles[i][j] += max(triangles[i+1][j], triangles[i+1][j+1])
    triangles.pop() # don't need last row anymore

print(triangles)
