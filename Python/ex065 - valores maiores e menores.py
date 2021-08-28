comfirm = 'S'
count = maior = menor = soma = n = 0

while comfirm == 'S':
    n = int(input("Digite um numero: "))
    soma = soma + n
    count = count + 1
    if count == 1 :
        maior = menor = n
    else :
        if n > maior :
            maior = n
        if n < menor :
            menor = n
    comfirm = str(input("Voce deseja continuar?[S/N]: ")).strip().upper()[0]
media = soma / count
print('''A soma dos {} valores foi {},
com uma media de {:.2f},
o maior valor foi {} e o menor {}.'''.format(count, soma, media, maior, menor))
