cont = 0
num = int(input('Digite o número: '))
for c in range(1, num+1):
    if num%c == 0:
        cont += 1
if cont > 2:
    print('Não eh primo')
else:
    print('Eh primo')