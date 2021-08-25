from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = date.today().year - ano_nascimento

if idade < 18 :
    saldo = abs(idade - 18)
    saldo_ano = date.today().year + saldo
    print("Voce ainda nao precisa se alistar.Ainda faltam {} anos. voce terá que ce alistar em {}".format(saldo, saldo_ano))
elif idade == 18 :
    print("Voce já tem idade para se alistar.")
elif idade > 18 :
    print("Voce já passou da idade de se alistar.ou já se alistou")
