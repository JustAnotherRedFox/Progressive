school = []

while True:
    name = str(input('Name: '))
    score1 = int(input("Score 1: "))
    score2 = int(input("Score 2: "))
    media = (score1 + score2) / 2
    school.append([name, [score1, score2], media])

    answer = input('Continue? [Y/N]: ')

    if answer in 'Yy':
        continue

    elif answer in 'Nn':
        break

print('-=-' * 20)
print(f"{'ID':<4}{'Name':<10}{'Media':>8}")
print('-' * 60)

for i, stud in enumerate(school):
    print(f"{i:<4}{stud[0]:<10}{stud[2]:>8.1f}")

while True:
    answer = str(input("Show Table? [Y/N] \n> "))

    if  answer in 'Yy':
        ident = int(input("Type the student ID: "))

        print(f"Name: {school[ident][0]} \nScore: {school[ident][1]}")

    elif answer in 'Nn':
        print("You're Welcome")
        break

    else:
        continue