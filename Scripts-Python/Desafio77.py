palavras = 'Mamao', 'Cafe', 'Brocolis', 'HunterXHunter', 'Coronavirus', 'Milharina', 'Ovo', 'Anime', 'Otaku', 'Maca', 'Vaca', 'Corona virus', 'Atila foda', 'Python', 'Dark Souls'

for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aiou':
            print(letra, end=' ')
    print()