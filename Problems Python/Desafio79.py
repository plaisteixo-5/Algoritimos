num = list()
n = 0

while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Número adicionado!')
    else:
        print('O número já está na lista. Tente outro!')
    c = str(input('Deseja continuar? [S/N]'))
    if c in 'Nn':
        break
num.sort()
print(f'Os valor digitados foram {num}')