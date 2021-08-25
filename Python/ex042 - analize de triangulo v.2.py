a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))

if a < b + c and b < c + a and c < a + b :
    print("Pode formar um triangulo.")
    if a == b == c :
        print("Será um triangulo equilatero")
    elif a != b == c or b != c == a or c != a == b :
        print("Será um triangulo Isosceles")
    elif a != b != c :
        print("Será um triangulo Escaleno")
else :
    print("Nao pode formar um triangulo")
