from random import randint
from time import sleep

numbers = list()
games = list()
numberOfTimes = int(input("how many times: "))
total = 1
while total <= numberOfTimes:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in numbers:
            numbers.append(num)
            count += 1

        if count >= 6:
            break
    numbers.sort()
    games.append(numbers[:])
    numbers.clear()
    total += 1

print("Sorting games...")
for i, item in enumerate(games):
    sleep(1 + i)
    print(f"game {i +1}: {item}")

    
    