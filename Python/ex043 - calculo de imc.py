print('-'*60)
print('{:-^60}'.format(" Índice de Massa Corporal "))
print('-'*60)
nome = str(input("Digite seu nome: ")).strip()
peso = float(input("Digite seu peso, Kg.: "))
altura = float(input("Digite sua altura, m.: "))
imc = peso / (altura * altura)

if imc < 18.5 :
    msg = "\033[33mAbaixo do Peso\033[m"
elif imc >= 18.5 and imc < 25 :
    msg = "\033[32mPeso Ideal\033[m"
elif imc >= 25 and imc < 30 :
    msg = "\033[33mSobrepeso\033[m"
elif imc >= 30 and imc < 40 :
    msg = "\033[31mObesidade\033[m"
elif imc > 40 :
    msg = "\033[31mObesidade Mórbida\033[m"
print('-=-'*20)
print("Cadastro : {}".format(nome.title()))
print("Peso : {:.2f}".format(peso))
print("altura : {:.2f}".format(altura))
print("IMC : {:.1f} :{:^30}".format(imc, msg))
print('-=-'*20)
