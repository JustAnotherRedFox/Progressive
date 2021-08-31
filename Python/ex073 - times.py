times = ('atletico-MG', 'palmeiras', 'fortaleza', 'bragantino', 'flamengo', 'corintians', 'atletico-GO',
         'ceara', 'atletico-PR', 'internacional', 'santos', 'sao paulo', 'juventude', 'cuiaba', 'bahia')
pontos = (39, 35, 32, 32, 31, 27, 25, 24, 23, 23, 22, 22, 21, 20, 18)
print(f"os 5 primeiros colocados: {times[:5]}")
print(f"os 4 ultimos colocados {times[-4:]}")
print(f"tabela em ordem alfabetica: {sorted(times)}")
print(f"posiçao do bahia: {times.index('bahia') + 1}ª posiçao")
