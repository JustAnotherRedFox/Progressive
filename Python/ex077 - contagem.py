palavras = ('gratis', 'aprender', 'python', 'diaadia', 'televisao')

for count in palavras:
    print(f"\nna palavra {count} temos as vogais", end=' ')
    for letra in count:
        if letra.lower() in 'aeiou':
            print(f"{letra}", end=' ')
