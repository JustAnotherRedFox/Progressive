words = ('gratis', 'aprender', 'python', 'diaadia', 'televisao')

for word in words:
    print(f"\nna palavra {word} temos as vogais", end=' ')
    for l in word:
        if l.lower() in 'aeiou':
            print(l, end=' ')
