from time import sleep
nome = str(input("Digite seu nome: ")).strip().title()

print("\nHi {}, nice meet you!\n".format(nome))

print("analizando seu nome...")
sleep(1)
nome = nome.split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print("Seu primeiro nome é {},".format(primeiro_nome))
print("Seu ultimo nome é {}.".format(ultimo_nome))
