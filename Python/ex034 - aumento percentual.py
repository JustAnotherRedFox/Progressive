salario = float(input("Digite o salario de funcionario: R$"))

print('''\nconsiderando : 
salario > R$1.250 -> aumento de 10%
salario < R$1.250 -> aumento de 15%\n''')

if salario > 1250 :
    novo_salario = salario + (salario * (10/100))
elif salario < 1250 :
    novo_salario = salario + (salario * (15/100))

print("o salario do funcionario que éra de {:.2f} passará a ser {:.2f}".format(salario, novo_salario))
