from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano_nascimento

if idade <= 9 :
    print("Categoria CNN : Mirin.")
elif idade <= 14 :
    print("categoria CNN : Infantil")
elif idade <= 19 :
    print("Categoria CNN : junior")
elif idade <= 25 :
    print("Categoria CNN : Senior")
elif idade > 25 :
    print("Categoria CNN: Master")
