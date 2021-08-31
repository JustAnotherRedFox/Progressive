lista = ('pao', 10.58, 'manteiga', 5.99, 'ovos', 30.00)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f"{lista[c]:.<20}", end='')
    else:
        print(f"R${lista[c]:.2f}")
