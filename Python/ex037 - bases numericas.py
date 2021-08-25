n = int(input("Digite um numero inteiro: "))

menu = int(input('''Digite sua escolha para conversao: 
[1] para conversao binaria
[2] para conversao octal
[3] para conversao hexadecimal
Digite sua escolha: '''))

if menu == 1 :
    print("{} convertido para base Binaria será {}".format(n, bin(n)[2:]))
elif menu == 2 :
    print("{} convertido para base Octal será {}".format(n, oct(n)[2:]))
elif menu == 3 :
    print("{} convertido para base Hexadecimal será {}".format(n, hex(n)[2:]))
else:
    print("\033[31mOpção invalida!\033[m")

