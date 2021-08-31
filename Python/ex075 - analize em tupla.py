valor = (int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")))

print(f"voce digitou os valores {valor}")
print(f"o numero 9 apareceu: {valor.count(9)} vezes")
if 3 in valor:
    print(f"o numero 3 aparece na {valor.index(3)+1}ª posiçao")
par = 0
for c in range(0, 4):
    if valor[c] % 2 == 0:
        par = par + 1
print(f"possui {par} numeros pares")