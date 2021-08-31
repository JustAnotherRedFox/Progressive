# import this
while True:
    numero = int(input("Digite um numero de [0 - 10]: "))
    if 10 >= numero >= 0 :
        break
numero_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
print(f"O numero por extenso é {numero_extenso[numero]}")
