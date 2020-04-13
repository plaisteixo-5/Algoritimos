maior = 0
menor = 0
media = 0
cont = 0
comando = 'S'

while comando not in 'Nn':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = num
        menor = num
        media += num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        media += num
    cont += 1
    comando = str(input('Deseja continua? [S/N]'))
print('''
Você digitou {} números
O maior foi {}
O menor foi {}
E a média entre eles é de {}'''.format(cont,maior,menor,media/cont))