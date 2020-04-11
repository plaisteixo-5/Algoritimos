num = list()
c = ''

while True:
    num.append(int(input('Digite um número: ')))
    c = str(input('Você deseja continuar? [S/N]'))
    if c in 'Nn':
        break
print(f'Você digitou {len(num)} números')
num.sort(reverse=True)
print(f'{num}')
if 5 in num:
    print('Tem o número 5 na lista de números')
else:
    print('Não tem o número 5 na lista de números')