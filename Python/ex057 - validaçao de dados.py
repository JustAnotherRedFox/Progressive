'''comfirm = 'negade'
while comfirm != 'aproved' :
    genero = str(input("Digite seu genero[M/F]: ")).strip().upper()
    if genero == 'F' or genero == 'M' :
        print("Dados salvos.")
        comfirm = 'aproved'
    else:
        print("Dados invalidos, tente novamente.")'''
genero = str(input("Digite seu genero[F/M]: ")).strip().upper()
while genero not in 'FM' :
    genero = str(input("\033[31mGenero Invalido\033[m, \nPor Favor informe seu genero[F/M]: ")).strip().upper()

print("Cadastro finalizado com sucesso.")
