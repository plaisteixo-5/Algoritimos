from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
jP = randint(0,2)

jogada = int(input('''Escolha uma das opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
'''))

print('-='*10)
if jP == 0:
    if(jogada == 1):
        print('Empatou')
    elif(jogada == 2):
        print('O jogador venceu!!')
    elif(jogada == 3):
        print('O jogador perdeu :(')
    else:
        print('Opção inválida. Tente novamente')

elif jP == 1:
    if(jogada == 1):
        print('O jogador perdeu :(')
    elif(jogada == 2):
        print('Empatou')
    elif(jogada == 3):
        print('O jogador venceu!!')
    else:
        print('Opção inválida. Tente novamente')

elif jP == 2:

    if(jogada == 1):
        print('O jogador venceu!!')
    elif(jogada == 2):
        print('O jogador perdeu :(')
    elif(jogada == 3):
        print('Empatou')
    else:
        print('Opção inválida. Tente novamente')

else:
    print('Opção inválida. Tente novamente')    
print('-='*10)