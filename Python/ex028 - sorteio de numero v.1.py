from random import randint
from time import sleep
print('-=-'*20)
print("\033[36mVou pensar em um numero de 1 a 5 tente advinhar!\033[m")
print('-=-'*20)
player = int(input("\nDigite um numero: "))

print("\nPensando...\n")
sleep(1)

cpu = randint(1, 5)

if cpu == player :
    print("Parabens voce acertou!")
else :
    print("Que pena voce perdeu o numero que pensei foi {}".format(cpu))
