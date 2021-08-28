pt = int(input("Digite o primeito termo da PA: "))
r = int(input("Digite a razao: "))
decimo = pt + (10 - 1) * r
for count in range(pt, decimo + 1, r) :
    print(count, end=' ')
