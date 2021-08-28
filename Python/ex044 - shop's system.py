print('\033[33m-=-\033[m'*20)
print('{:-^60}'.format(" Santos&sampaio's shop "))
print('\033[33m-=-\033[m'*20)
preco = float(input("Valor total da compra: R$"))
menu = int(input('''Digite seu metodo de pagamento:
[\033[36m1\033[m] à vista em Dinheiro/cheque.
[\033[36m2\033[m] à vista no cartão.
[\033[36m3\033[m] 2x no cartão.
[\033[36m4\033[m] 3x ou mais no cartão.
[\033[36m5\033[m]Para cancelar a compra.
opção: '''))

if menu == 1 :
    valor = preco - (preco * (10/100))
    print("Você Recebeu 10% de desconto, o valor total da compra é R${:.2f}.".format(valor))
elif menu == 2 :
    valor = preco - (preco * (5/100))
    print("Você Recebeu 5% de desconto, o valor total da compra é R${:.2f}.".format(valor))
elif menu == 3 :
    valor = preco / 2
    print("O Valor total da compra é R${:.2f}, e será pago em 2 parcelas de R${:.2f}.".format(preco, valor))
elif menu == 4 :
    vezes = int(input("Quantas vezes deseja parcelar? "))
    precoj = preco + (preco * (20/100))
    valor = precoj / vezes
    print("O valor total da compra é R${:.2f},com 20% de juros e será pago em {} Parcelas de R${:.2f}.".format(preco, vezes, valor))
elif menu == 5 :
    print("Compra cancelada")
else:
    print("\033[31mOpção Invalida\033[m.")
print("\033[32mObrigado pela Preferencia, Um Bom Dia!\033[m")