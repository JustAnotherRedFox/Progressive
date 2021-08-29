from random import randint, choice
print("Vamos jogar par ou impar.")
vitorias = 0

while True :
    player_choice = str(input("Par ou Impar?: ")).strip().lower()
    while player_choice not in 'parimpar':
        print("\033[31mEscolha Invalida\033[m, tente novamente!")
        player_choice = str(input("Par ou Impar?: ")).strip().lower()

    player_num = int(input("Escolha um numero[0 - 10]: "))
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while player_num not in lista:
        print("\033[31mNumero Invalido\033[m, tente novamente!")
        player_num = int(input("Escolha um numero[0 - 10]: "))

    cpu_num = randint(0, 10)
    print(f"O numero que escolhi foi {cpu_num}")
    print(f"{player_num} + {cpu_num} dá {player_num + cpu_num}")
    tipo = (cpu_num + player_num) % 2

    if player_choice == 'par':
        if tipo % 2 == 0:
            print("Voce venceu!")
            vitorias = vitorias + 1
        else:
            print("Voce perdeu!")
            break
    elif player_choice == 'impar':
        if tipo % 2 != 0:
            print("Voce ganhou!")
            vitorias = vitorias + 1
        else:
            print("Voce perdeu!")
            break

print(f"Voce teve {vitorias} vitorias!")
