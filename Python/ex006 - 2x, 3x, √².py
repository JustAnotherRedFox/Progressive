from math import sqrt
n = int(input("Digite um numero: "))
# dobro = n * 2
# triplo = n * 3
# raiz = n * (1/2)
print('''O Dobro de {} é {}
O Triplo : {}
A raiz quadrada : {:.1f}'''.format(n, n * 2, n * 3, sqrt(n)))
