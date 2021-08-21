#radar de velocidade, max km/h 80, r$7.00 / km/h acima
print('-'*50)
print('{:-^50}'.format(" Radar de Velocidade "))
print('-'*50)
print("O Limite de velocidade desta rodovia é : 80Km/h.")
print("A Multa será de R$7.00 por km passado do limite.")
print('-'*50)
velocidade = float(input("Digite a velocidade do carro:\nkm/h: "))
multa = (velocidade - 80) * 7.00
if velocidade > 80 :
    print("Você ultrapassou a velocidade maxima permitida por \033[31m{:.0f}\033[mKm/h e terá de pagar uma multa de R$\033[31m{:.2f}\033[m.".format(velocidade, multa))
print("Dirija com Segurança. Um bom dia!")
