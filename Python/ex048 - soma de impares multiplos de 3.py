contagem = 0
soma = 0
for count in range(1, 501):
    if count % 3 == 0 and count % 2 != 0:
        soma = soma + count
        contagem = contagem + 1
print("Os {} numeros impares somados dá {}".format(contagem, soma))
