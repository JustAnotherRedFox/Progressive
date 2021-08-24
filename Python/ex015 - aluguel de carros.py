dias_aluguel = int(input("Por quantos dias o carro foi alugado? "))
km = int(input("Rodou por quantos quilometros? "))

total = (dias_aluguel * 60) + (km * 0.15)

print('''\nVocê alugou o carro por {} dias e Rodou {}km,
considerando, R$60.00/dia e R$0.15/km\n'''.format(dias_aluguel, km))
print("O Valor total a pagar será de R${:.2f}".format(total))
