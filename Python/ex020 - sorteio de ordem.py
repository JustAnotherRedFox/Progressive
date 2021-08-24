from random import shuffle
nome1 = str(input("Digite um nome: "))
nome2 = str(input("Digite outro nome: "))
nome3 = str(input("Digite o 3º nome: "))
nome4 = str(input("Digite o 4º nome: "))

nome_lista = [nome1, nome2, nome3, nome4]
shuffle(nome_lista)

print("A nova ordem de nome será : {}".format(nome_lista))
