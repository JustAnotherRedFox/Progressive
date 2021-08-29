count_younger_females = count_male = count_younger = 0
while True:
    genero = str(input("Digite o Gênero[F/M]: ")).strip().upper()
    if genero in "FM":
        idade = int(input("Digite a Idade: "))
        if idade < 0 or idade > 150:
            print("\033[31mIdade Invalida\033[m, tente novamente.")
        else:
            if idade >= 18 :
                count_younger = count_younger + 1
            if genero == 'M' :
                count_male = count_male + 1
            if genero == 'F' and idade < 20 :
                count_younger_females = count_younger_females + 1
            comfirm = str(input("Deseja continuar?: ")).strip().upper()
            if comfirm == 'S' :
                print("")
            elif comfirm == 'N' :
                break
            else:
                print("\033[31mOpção Invalida\033[m, Tente novamente.")
    else:
        print("\033[31mGênero Invalido\033[m, tente novamente.")
print(f'''Programa encerrado, Com: 
{count_male} homens, 
{count_younger_females} mulheres com menos de 20 anos, e 
{count_younger} pessoas com Mais de 18 anos.''')
