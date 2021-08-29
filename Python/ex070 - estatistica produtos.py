total = count_caro = preco_barato = count = 0
produto_barato = ' '
while True:
    count = count + 1
    produto = str(input("Digite um Produto: ")).strip().lower()
    preco = float(input("Digite o Preço do Produto: R$"))
    if preco < 0 :
        print("\033[31mPreço Invalido\033[m, tente novamente.")
    else:
        total = total + preco
        if count == 1 or preco < preco_barato :
            preco_barato = preco
            produto_barato = produto
        if preco > 1000 :
            count_caro = count_caro + 1
        comfirm = str(input("deseja continuar?: ")).strip().upper()
        if comfirm == 'S' :
            print('-'*20)
        elif comfirm == 'N' :
            break
        else:
            print("\033[31mOpção Invalida\033[m, tente novamente")
print(f'''
O total das compras foi : R${total:.2f},
Um total de {count} produtos,
{count_caro} produtos acima de R$1000.00,
O produto mais barato foi {produto_barato} por R${preco_barato:.2f}''')
