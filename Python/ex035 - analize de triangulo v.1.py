print('\033[36m-=-\033[m'*20)
print('\033[33m{:-^60}\033[m'.format(" Analizador de Triangulo "))
print('\033[36m-=-\033[m'*20)
reta1 = float(input("Digite a 1º reta do triangulo a ser analizado: "))
reta2 = float(input("Digite a 2º reta do triangulo: "))
reta3 = float(input("Digite a 3º reta do triangulo:"))

if reta1 < reta2 + reta3  and reta2 < reta1 + reta3 and reta3 < reta1 + reta2 :
    print("Pode formar um triangulo")
else :
    print("Não pode formar um triangulo")
