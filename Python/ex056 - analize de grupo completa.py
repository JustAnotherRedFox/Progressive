soma_idade = 0
older_man = 0
older_name = ''
younger_ladies = 0
for count in range(1, 5) :
    print('{:=^20}'.format(" {}º Pessoa ".format(count)))
    nome = str(input("Digite o nome: ")).strip().title()
    idade = int(input("Digite a idade: "))
    genero = str(input("Digite o Genero[F/M]: ")).strip().upper()
    soma_idade = soma_idade + idade
    media_idade = soma_idade / 4
    if idade > older_man and genero == 'M' :
        older_man = idade
        older_name = nome
    if genero == 'F' and idade < 20 :
        younger_ladies = younger_ladies + 1
print('''Do grupo acima a media de idade é {},
o Homem mais velho se chama {} e tem {} anos,
e possui {} jovens com menos de 20 anos.'''.format(media_idade, older_name, older_man, younger_ladies))
