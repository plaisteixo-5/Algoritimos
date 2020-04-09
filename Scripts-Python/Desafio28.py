from random import randint

num = int(input('Tente adivinhar o número do computador: '))
numC = randint(0,5)

if(num == numC):
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez')

