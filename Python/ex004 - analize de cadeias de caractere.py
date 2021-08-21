frase = str(input("Digite algo: "))

tipo = type(frase)
if tipo == str:
    tipo = "Texto"
if tipo == int:
    tipo = "Numero Inteiro"
if tipo == float:
    tipo = "Numero Real"
if tipo == bool:
    tipo = "Booleano"


print("tipo : {}".format(tipo))
print("- é alfanumerico ? {}".format(frase.isalnum()))
print("- é alfabetico ? {}".format(frase.isalpha()))
print("- é um numero ? {}".format(frase.isnumeric()))
print("- está capitalizado ? {}".format(frase.istitle()))
print("- é composto só por espaço ? {}".format(frase.isspace()))
print("- está em minusculo? {}".format(frase.islower()))
print("- está em Maiusculo ? {}".format(frase.isupper()))
