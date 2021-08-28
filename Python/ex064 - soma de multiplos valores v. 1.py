soma = count = 0
num = int(input("Digite um numero inteiro(999 para parar): "))
while num != 999 :
    soma = soma + num
    count = count + 1
    num = int(input("Digite um numero inteiro(999 para parar): "))
print("A soma dos {} valores foi {}".format(count, soma))
