lista = list()
impares = list()
pares = list()
n = 0
C = ''

while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    c = str(input('Deseja continuar? [S/N]'))
    if c in 'Nn':
        break
print(f'A lista digitada foi {lista}\nOs números pares dela são {pares}\nE os impares são {impares}')