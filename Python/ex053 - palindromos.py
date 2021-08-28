frase = str(input("Digite uma frase: ")).strip().lower()

frase_striped = frase.replace(' ', '')
frase_reverse = frase_striped[::-1]

if frase_reverse == frase_striped :
    print("Temos um palindromo")
else :
    print("Nao é um palindromo a frase {} ao contrario é {}".format(frase, frase_reverse))
