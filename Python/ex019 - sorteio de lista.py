from random import choice
nome1 = str(input("Digite um nome: "))
nome2 = str(input("Digite o 2º nome: "))
nome3 = str(input("Digite o 3º nome: "))
nome4 = str(input("Digite o 4º nome: "))

lista_nomes = [nome1, nome2, nome3, nome4]
nome_escolhido = choice(lista_nomes)

print("o nome sortiado foi : {}.".format(nome_escolhido))
