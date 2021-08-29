
while True:
    n = int(input("Digite um numero: "))
    if n < 0:
        break
    for count in range(1, 11):
        print(f"{n} x {count:2} : {count * n:2}")
        count = count + 1
