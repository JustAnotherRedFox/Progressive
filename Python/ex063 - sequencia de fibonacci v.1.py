#input do usuario
termos = int(input("Quantos termos voce deseja ver?: "))

# input de valores do while
count = 3
t1 = 0
t2 = 1
print(t1, "->", t2, end=' -> ')

# calculo da Sequencia de fibonacci
while count <= termos :
    t3 = t2 + t1
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    count = count + 1
print("Fim")
print("\nFim da sequencia")
