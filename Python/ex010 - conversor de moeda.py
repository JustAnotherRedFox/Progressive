print("{:-^60}".format(" Conversor de Moedas "))
BRL = float(input("Digite quantos Reais voce possui: R$"))

# Relaçao de agosto/2021
USD = 0.1843
EUR = 0.1576
YEN = 20.2224
RMB = 1.1979
KWD = 0.0554

print("Com R${:.2f}, Voce pode comprar U${:.2f}(DOLAR).".format(BRL, BRL * USD))
print("Com R${:.2f}, Voce pode comprar €{:.2f}.(EURO)".format(BRL, BRL * EUR))
print("Com R${:.2f}, Voce pode comprar ¥{:.2f}(YENS).".format(BRL, BRL * YEN))
print("Com R${:.2f}, Voce pode comprar 元{:.2f}(RMB ou YUAN chines).".format(BRL, BRL * RMB))
print("Com R${:.2f}, Voce pode comprar د.ك{:.2f}(KWD ou Dinar do Kuwait).".format(BRL, BRL * KWD))
