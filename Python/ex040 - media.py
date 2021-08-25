nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0 :
    print("\033[31mAluno Reprovado\033[m")
elif media >= 5.0 and media < 7.0 :
    print("\033[33mAluno de Recuperaçao\033[m")
elif media >= 7.0 :
    print("\033[32mAluno Aprovado\033[m")
