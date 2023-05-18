#show: total number of registred, the heavier, the lighter

person = []
people = []
maxValue = minValue = 0

while True:
    person.append(str(input('Name: ')))
    person.append(float(input('Weight: ')))

    if len(person) == 0:
        maxValue = minValue = person[1]
    
    else:
        if person[1] > maxValue:
            maxValue = person[1]
        
        if person[1] < minValue:
            minValue = person[1]

    people.append(person[:])
    person.clear()

    comfirm = input('want to continue? \n> ')
    
    if comfirm in 'nN':
        break

print(f"the registred data is: {people}")
print(f"{len(people)} people was registred")

print(f"the heavier person Is: ", end='')
for p in people:
    if p[1] == maxValue:
        print(p[0], end='')

print()

print(f"the lighter person Is: ", end='')
for per in people:    
    if per[1] == minValue:
        print(per[0], end='')
