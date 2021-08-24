from time import sleep
n = int(input("digite um numero: "))

unidade =  n // 1 % 10
dezena =   n // 10 % 10
centena =  n // 100 % 10
milhar =   n // 1000 % 10

print("\033[32mAnalizando...\033[m")
sleep(1)

print('''O numero {} possui:
{} unidades,
{} dezenas,
{} centenas e,
{} milhares.'''.format(n, unidade, dezena, centena, milhar))
