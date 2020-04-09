d = float(input('Digite a distância da viagem em Km: '))
if(d <= 200):
    print('O preço da passagem é de R${} reais'.format(d*0.50))
else:
    print('Sua passagem custará R${}'.format(d*0.45))
