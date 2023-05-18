# Read multiple values an put on a list
# from the main list create two lists one with only even numbers and other with only odd numbers
# Show the three lists



values = []
even = []
odd = []

while True:
    val = int(input('type a number: '))

    values.append(val)

    confirm = input('do you want to continue?[Y/N] \n> ').upper()[0]

    if confirm == 'N':
        break



for v in values:
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)

print(values)
print(even)
print(odd)