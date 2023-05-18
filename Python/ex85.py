values = [[], []]

for count in range(0, 7):
    value = int(input("type a number: "))

    if value % 2 == 0:
        values[0].append(value)
    else:
        values[1].append(value)

values[0].sort()
values[1].sort()
print(f"the pair numbers was {values[0]}")
print(f"the odd numbers was {values[1]}")