matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#matrix = [[78, 19, 12], [47, 20, 17], [56, 32, 12]]
mSum = 0
sum3rd = 0
greater2nd = 0

for r in range(0, 3):
    for c in range(0, 3):
        matrix[r][c] = int(input("type the number for col[{column}] and row[{row}]: "))

for r in range(0, 3):
    for c in range(0, 3):
        if matrix[r][c] % 2 == 0:
            mSum += matrix[r][c]
        
        if r == 1 and c == 0:
            greater2nd = matrix[r][c]
            
        elif r == 1:
            if matrix[r][c] > greater2nd:
                greater2nd = matrix[r][c]

    sum3rd += matrix[r][2]

print(f"the sum of all pair numbers is {mSum}")
print(f"the sum of all values in the 3rd collumn is {sum3rd}")
print(f"the greater value in the 2nd row is {greater2nd}")
