numeros = []
posições = []
maior = 0
menor = 999

for c in range(0,5):
    numeros.append(int(input('DIgite um número: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        elif numeros[c] < menor:
            menor = numeros[c]

print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i} ', end='')

print()
print(f'O menor valor digitado foi {menor} mas posiçõrd ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i} ', end='')