soma = 0
contagem = 0
par = 0
for count in range(1, 7) :
    n = int(input("Digite o {}º numero: ".format(count)))
    if n % 2 == 0:
        soma = soma + n
        par = par + 1
    else :
        soma = soma + 0
    contagem = contagem + 1
print("Voce imformou {} valores,E a soma dos {} valores pares é {}".format(contagem, par, soma))
