matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#matrix = [[12, 32, 16], [60, 35, 20], [60, 90, 45]]


for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f"type the number for col[{column}] and row[{row}]: "))

for r in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrix[r][c]:^4}]", end='')
    print()