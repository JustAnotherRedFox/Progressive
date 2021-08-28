soma = count = 0
while True:
    n = int(input("digite um numero(999 para parar): "))
    if n == 999:
        break
    soma = soma + n
    count = count + 1
print(f"a soma dos {count} valores digitados será {soma}.")
print("a soma dos {} valores digitados será {}.".format(count, soma))
