n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
menu = 0
while menu != 7 :
    menu = int(input('''Que operaçao voce deseja fazer?
    [1] para somar
    [2] para subtrair
    [3] para multiplicar
    [4] para dividir
    [5] para definir qual o Maior e menor
    [6] para mudar os numeros
    [7] para fechar o programa
    sua opçao: '''))
    if menu == 1:
        print("{} + {} = {}".format(n1, n2, n1 + n2))
    elif menu == 2:
        print("{} - {} = {}".format(n1, n2, n1 - n2))
    elif menu == 3:
        print("{} x {} = {}".format(n1, n2, n1 * n2))
    elif menu == 4:
        print("{} Dividido por {} é {:.1f}".format(n1, n2, n1 / n2))
    elif menu == 5:
        if n1 > n2 :
            print("{} é o maior e {} o menor.".format(n1, n2))
        elif n2 > n1 :
            print("{} é o maior e {} o menor.".format(n2, n1))
        elif n1 == n2 :
            print("Ambos os valores digitados sao iguais")
    elif menu == 6:
        n1 = int(input("Qual o novo primeiro numero?: "))
        n2 = int(input("Qual o novo segundo numero?: "))
print("Programa encerrado.")