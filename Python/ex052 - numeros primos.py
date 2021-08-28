n = int(input("Digite um numero: "))

divisao = 0
for count in range(1, n + 1) :
    if n % count == 0 :
        divisao = divisao + 1
        print("\033[31m{}\033[m".format(count), end=' ')
    else:
        print("\033[32m{}\033[m".format(count), end=' ')
if divisao > 2 :
    print("\n{} não é primo pois foi divisivel {} vezes".format(n, divisao))
elif divisao <= 2 :
    print("\n{} é um numero primo pois só foi divisivel por 2 numeros, 1 e ele mesmo".format(n))
