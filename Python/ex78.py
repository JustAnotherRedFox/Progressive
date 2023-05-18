values = []
maxValue = []
minValue = []

for c in range(0, 5):
    values.append(input('type a number: '))

print(f'The typed numbers are: ', end='')
for i in values:
    print(i, end=' ')

for i, v in enumerate(values):
    if v is max(values):
        maxValue.append(i)

    if v is min(values):
        minValue.append(i)

print(f'\nThe biggest values are: {max(values)} on indexes {maxValue}')
print(f'The Smallest values are: {min(values)} on indexes {minValue}')