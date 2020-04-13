contG = 0
contA = 0
contD = 0
n = 0

while n != 4:
    n = int(input())
    if n == 1:
        contA += 1
    if n == 2:
        contG += 1
    if n == 3:
        contD += 1
print('MUITO OBRIGADO')
print(f'Alcool: {contA}')
print(f'Gasolina: {contG}')
print(f'Diesel: {contD}')