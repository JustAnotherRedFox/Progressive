# teorema de Pitágoras
# hipotenusa² : cateto oposto² + cateto adjacente²
from math import sqrt
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hipo2 = (cateto_adjacente ** 2) + (cateto_oposto ** 2)
hipo = sqrt(hipo2)

print("A hipotenusa será {:.2f}.".format(hipo))
