vC = float(input('Digite o valor da casa: '))
s = float(input('Digite o valor do seu salário: '))
t = int(input('Em quanto tempo pretende pagar? '))

if(((vC/t)*0.30)>s):
    print('O empréstimo foi negado, pois seu salário é inferior à 30% do valor total do valor da casa')
else:
    print('O valor a ser pago mensalmente será de R${:.2f} reais por {} anos'.format(vC/(t*12),t))