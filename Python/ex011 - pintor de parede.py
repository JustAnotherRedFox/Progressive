largura = float(input("Digite a largura da parede[M]: "))
altura = float(input("Digite a altura da parede[M] "))

area = largura * altura
tinta = area / 2

print("Considerando 1l de tinta -> 2m² ")
print("Sua parede possui {:.0f}m² e gastaria {:.2f}l de tinta para pinta-la.".format(area, tinta))
