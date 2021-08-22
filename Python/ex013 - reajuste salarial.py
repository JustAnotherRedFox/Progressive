salario = float(input("Digite o salario do funcionario: R$"))

salario_novo = salario + (salario * (15/100))

print('''O funcionario que recebia R${:.2f}, 
com 15% de aumento irá passar a receber R${:.2f}.'''.format(salario, salario_novo))
