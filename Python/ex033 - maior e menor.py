n1 = int(input("digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))

if n1 == n2 :
    print("os dois valores são iguais!")
elif n1 > n2 :
    print("{} é o maior valor e {} o menor.".format(n1, n2))
elif n1 < n2 :
    print("{} é o maior valor e {} o menor".format(n2, n1))
