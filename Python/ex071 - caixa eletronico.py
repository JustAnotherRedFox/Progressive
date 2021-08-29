saque = int(input("Que Valor voce quer sacar: R$"))
if saque < 0 :
    print("Opção Invalida, tente novamente")
else:
    valor_total = saque
    cedula50 = 50
    cedula20 = 20
    cedula10 = 10
    cedula1 = 1
    cedula50_total = cedula20_total = cedula10_total = cedula1_total = 0

    while True:
        if cedula50 <= valor_total:
            valor_total = valor_total - cedula50
            cedula50_total = cedula50_total + 1
            if valor_total == 0:
                break
        elif cedula20 <= valor_total:
            valor_total = valor_total - cedula20
            cedula20_total = cedula20_total + 1
            if valor_total == 0:
                break
        elif cedula10 <= valor_total:
            valor_total = valor_total - cedula10
            cedula10_total = cedula10_total + 1
            if valor_total == 0:
                break
        elif cedula1 <= valor_total:
            valor_total = valor_total - cedula1
            cedula1_total = cedula1_total + 1
            if valor_total == 0:
                break

print(f'''Com o saque de {saque}, serao :
{cedula50_total} cedulas de R$50,
{cedula20_total} cedulas de R$20,
{cedula10_total} celulas de R$10 e,
{cedula1_total} ceddulas de R$1''')
