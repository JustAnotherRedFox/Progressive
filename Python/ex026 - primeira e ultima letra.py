from time import sleep
frase = str(input("Digite um frase: ")).strip().lower()
letra = str(input("Qual letra você deseja analizar? ")).strip().lower()

print("\nAnalizando a Frase...\n")
sleep(1)

contagem = frase.count('{}'.format(letra))
primeira_ocorrencia = frase.find('{}'.format(letra))
ultima_ocorrencia = frase.rfind('{}'.format(letra))

print("Na frase {}...".format(frase.title()))
print("A letra '{}' aparece {} vezes.".format(letra.upper(), contagem))
print("A Primeira letra '{}' apareceu na posição {}.".format(letra.upper(), primeira_ocorrencia + 1))
print("A Ultima letra '{}' apareceu na posição {}.".format(letra.upper(), ultima_ocorrencia + 1))
