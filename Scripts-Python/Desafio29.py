v = float(input('Digite a velocidade do carro: '))

if(v > 80):
    print('Você foi multado!')
    print('Sua multa foi de R${:.4} reais'.format((v-80)*7))
else:
    print('Parabéns guerreiro, vc fez o minimo seu bosta')