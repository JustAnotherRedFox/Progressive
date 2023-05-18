def tuples():

    breakfast = ('brot', 'kaffee', 'käse', 'milch')

    #when only list the tuple items is enough
    for i in breakfast:
        print(i)

    print('-'*25)

    #when the index(improvised, count) is needed
    for i in range(0, len(breakfast)):
        print(f'{breakfast[i]} on index {i}')

    print('-'*25)

    #when the real index data is needed
    for i, item in enumerate(breakfast):
        print(f'{item} on index {i}')



def lists():
    values = list()  #can also be write as: values = []
    cap = int(input('digite how many Values You want to insert\n> '))

    for count in range(0, cap):
        values.append(input('Type a Value: '))

    for i, v in enumerate(values):
        print(f'on index {i} is stored the value {v}')

def composedLists():
    people = []
    person = []
    for c in range(0, 3):
        person.append(str(input('type the name: ')))
        person.append(int(input('type the age: ')))

        people.append(person[:])
        person.clear()

    print(people)
#tuples()
#lists()
#composedLists()