from random import randint
print("de 1 a 10, tente advinhar que numero eu pensei")
player = int(input("Qual numero voce acha que pensei? "))
cpu = randint(1, 10)

while player != cpu :
    if player > cpu :
        print("Que pena, pensei em um numero um pouco menor!.")
        player = int(input("Tente de novo: "))
    elif player < cpu :
        print("Que pena, pensei em um numero um pouco maior!")
        player = int(input("tende de novo: "))

print("Parabens voce acertou!")