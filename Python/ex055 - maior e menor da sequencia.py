Mais_pesado = 0
Mais_leve = 0
for c in range(1, 6) :
    peso = float(input("Digite o peso da {}º pessoa: ".format(c)))

    if c == 1 :
        Mais_leve = peso
        Mais_pesado = peso
    else :
        if peso > Mais_pesado :
            Mais_pesado = peso
        if peso < Mais_leve :
            Mais_leve = peso

print("Do grupo acima o mais pesado tinha {:.1f}kg e o mais leve {:.1f}kg.".format(Mais_pesado, Mais_leve))
