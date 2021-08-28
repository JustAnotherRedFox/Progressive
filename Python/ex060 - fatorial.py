n = int(input("Digite um numero para calcular seu fatorial: "))
count = n
numero = n
while count != 1 :
    count = count - 1
    n = n * count
print("O fatorial de {} é {}.".format(numero, n))
