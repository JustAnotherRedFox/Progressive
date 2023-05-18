# Read multiple input values from user
# them show:
# 1. How many numbers are typed
# 2. listed in decreasing order
# 3. if the value 5 was typed or not

values = []

while True:
    values.append(int(input("type a Value: ")))

    comfirm = input('Want to continue?[Y/N]: ').upper()[0]

    if comfirm == 'N':
        values.sort(reverse=True)
        print(f'Quantity of typed numbers: {len(values)}')
        print(f'Typed numbers was: {values}')
    
        if 5 in values:
            print(f'The number 5 was typed and is in index {values.index(5)}')

        else:
            print("The number 5 wasn't typed")

        break