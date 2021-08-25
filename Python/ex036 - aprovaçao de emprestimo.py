valor_casa = float(input("Qual o valor da casa: R$"))
salario_comprador = float(input("Qual o seu salario: R$"))
financiamento_anos = int(input("Quantos anos de financiamento: \n"))

financiamento = (valor_casa / financiamento_anos) / 12
salario30 = salario_comprador * (30/100)

if financiamento > salario_comprador * (30/100) :
    print("\033[31mEmprestimo negado\033[m")
elif financiamento <= salario_comprador * (30/100) :
    print("Emprestimo \033[32mConcedido\033[m, A Prestação será de {:.2f} mensal.".format(financiamento))
