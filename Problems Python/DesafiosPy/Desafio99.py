def vMaior(n,maior):
    if n > maior:
        return n
    else:
        return maior

def maior():
    n = list()
    c = 'S'
    aux = 0
    maior = 0
    while c not in 'Nn':
        aux = int(input('Número: '))
        maior = vMaior(aux,maior)
        n.append(aux)
        c = str(input('Você deseja continuar?[S/N] '))
    print(f'Os valores digitados foram ',end='')
    for c in n:
        print(f'{c} ',end='')
    print(f'e o maior valor foi {maior}!!')

maior()


