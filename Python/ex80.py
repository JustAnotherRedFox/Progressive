# User Type 5 numbers
# Put on a List
# Already in  correct possition without sort()

numbers = []

for c in range(0, 5):
    value = int(input("type in a number: "))

    if c == 0 or value > numbers[-1]:
        numbers.append(value)
        print('value add to the end of the list')

    else:
        i = 0
        while i < len(numbers):
            if value <= numbers[i]:
                numbers.insert(i, value)
                print(f'value added in index {i}')
                break
            i += 1

print(numbers)