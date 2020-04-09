palavras = 'Mano', 'Battlefield', 'Coisa Nossa', 'Guaraná', 'Hunter', 'Magica', 'Milharina', 'Cuscuz', 'Cabelo'

for palavra in palavras:
    print(f'A palavra {palavra} tem as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()