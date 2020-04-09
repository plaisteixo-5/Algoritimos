r1 = int(input('Informe o valor da primeira reta: '))
r2 = int(input('Informe o valor da segunda reta: '))
r3 = int(input('Informe o valor da terceira reta: '))

if(r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1):
    print('Sim, podemos formar um triangulo com as retas {}, {} e {}!!'.format(r1,r2,r3))
    if(r1 == r2 and r2 == r3):
        print('O triângulo formado é equilátero')
    if r1 == r2 and r1 != r3 or r2 == r3 and r1 != r3 or r3 == r1 and r1 != r2:
        print('O triângulo é isóceles')
    if(r1 != r2 and r2 != r3 and r3 != r1):
        print('O triângulo é escaleno')
else:
    print('Não podemos construir um triângulo com as retas {}, {} e {} :('.format(r1,r2,r3))
