from time import sleep
nome = str(input("Digite seu nome: ")).strip().title()

print("Analizando seu nome...")
sleep(1)
primeiro_nome = nome.split()

print("\nSeu nome é {}".format(nome.title()))
print("Seu Nome em Maiusculo {}".format(nome.upper()))
print("Seu Nome em minusculo {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome é {} e possui {} letras".format(primeiro_nome[0], len(primeiro_nome[0])))
