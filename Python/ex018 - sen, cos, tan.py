# seno, cosseno e tangente
from math import *
angulo = float(input("Digite um angulo: "))

angulo_radiano = radians(angulo)
seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
tangente = tan(angulo_radiano)

print('''Analizando {:.0f}º seu seno será : {:.2f}º,
seu cosseno : {:.2f}º
e seu tangente : {:.2f}º'''.format(angulo, seno, cosseno, tangente))
