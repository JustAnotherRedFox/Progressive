from datetime import date
maioridade = 0
menoridade = 0
for count in range(1, 8) :
    ano_nascinmento = int(input("EM que ano a {}º pessoa nasceu? ".format(count)))
    idade = date.today().year - ano_nascinmento
    if idade >= 18 :
        maioridade = maioridade + 1
    elif idade < 18 : \
        menoridade = menoridade + 1
print("No grupo acima existem {} pessoas maior de idade e {} menor de idade.".format(maioridade, menoridade))
