values = []
while True:
    value = int(input('Type a Number: ')) #if not casted to integen, two or more digits numbers will not be sorted correctly

    if value not in values:
        values.append(value)
        print('Value Added successfully')

    elif value in values:
        print('Duplicated Entry. Value Not Added')
        

    comfirm = input('want to Continue? [Y/N] \n> ').upper()[0]

    if comfirm == 'N':
        values.sort()
        print(f'The inserted Values are: {values}')
        break