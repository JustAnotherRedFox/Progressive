nome_cidade = str(input("Digite o nome da sua cidade: ")).strip().lower()

nome_cidadeS = nome_cidade.split()
comfirm = "santo" in nome_cidadeS[0]

if comfirm :
    print("Sua cidade possui santo como primeiro nome")
elif "santo" not in nome_cidade :
    print("Sua cidade não possui 'santo' no nome")
else :
    print("Sua cidade Não possui 'santo' como primeiro nome")
