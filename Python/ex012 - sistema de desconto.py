print('-=-'*20)
print('{:^60}'.format(" \033[36mSantos&Santos's Shop\033[m "))
print('-=-'*20)
nome = str(input("Digite seu nome : ")).strip().title()
price = float(input("Digite o valor do produto: R$"))
pay_type = int(input('''Digite a forma de pagamneto:
[\033[34m0\033[m]á vista, dinheiro/cheque(10% de desconto)
[\033[34m1\033[m]á vista, cartão(5% de desconto)
[\033[34m2\033[m]em até 2x no cartão(sem desconto)
[\033[34m3\033[m]3x ou mais no cartão(20% de juros)
: '''))

if pay_type == 0 :
    topay = "R${:.2f}".format(price - (price * (10/100)))
    msg = "á vista dinheiro/cheque"
    deft = "Desconto : \033[32m10%\033[m"
elif pay_type == 1 :
    topay = "R${:.2f}".format(price - (price * (5/100)))
    msg = "á vista cartão"
    deft = "Desconto : \033[32m5%\033[m"
elif pay_type == 2 :
    topay = "R${:.2f} por mês.".format(price / 2)
    msg = "2x no cartão"
    deft = "Desconto : \033[37msem desconto\033[m"
elif pay_type == 3 :
    vez = int(input("Em quantas vezes deseja parcelar ? : "))
    topay = "R${:.2f} por Mês".format((price + (price * (20/100))) / vez)
    msg = " {}x no cartão".format(vez)
    deft = "Juros : \033[31m20%\033[m"

print('-=-'*20)
print("Cadastro : {}".format(nome))
print("Metodo de Pagamento : {}".format(msg))
print("{}".format(deft))
print("Total a Pagar : {}".format(topay))
print("\033[32mObrigado por Escolher Nossa Loja, Um Bom Dia!!\033[m")
print('-=-'*20)
