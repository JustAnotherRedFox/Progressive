pt = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razao: "))
count = 0
termino = 10
while count != termino :
    print(pt, end=' ')
    pt = pt + r
    count = count + 1
    if count == 10 :
        comfirm = str(input("\nvoce deseja continuar?[S/N]: ")).strip().upper()
        if comfirm == 'S':
            escolha = int(input("quantos mais fatoreais voce deseja ver?: "))
            count = count - escolha
        elif comfirm == 'N':
            print("")
        else:
            print("\n\033[31mERROR\033[m.")
print("programa Encerrado")
