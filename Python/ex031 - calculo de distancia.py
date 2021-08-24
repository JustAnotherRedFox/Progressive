distancia = float(input("Digite em km a distancia que deseja viajar: "))

print("\nconsiderando : distancia < 200km : R$0.50 e distancia > 200km : R$0.45\n")

if distancia <= 200 :
    preco = distancia * 0.50
elif distancia > 200 :
    preco = distancia * 0.45

print("O valor da passagem para uma viagem de {:.0f}km é R${:.2f}.".format(distancia, preco))
print("Boa Viagem!")
