matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = 0
somaTC = 0
maior = 0

for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input(f"DIgite um valor para [{c}, {i}]: "))
        if matriz[c][i] % 2 == 0:
            somaP += matriz[c][i]
        if i == 2:
            somaTC += matriz[c][i]
        if c == 1:
            if matriz[c][i] > maior:
                maior = matriz[c][i]
print('+='*5)
for c in range(0,3):
    for i in range(0,3):
        if i == 2:
            print(f'[{matriz[c][i]}]',end='')
        else:
            print(f'[{matriz[c][i]}]',end=' ')
    print()
print(f'A soma dos valores pares é {somaP}')
print(f'A soma dos valores da terceira coluna é {somaTC}')
print(f'E o maior valor da segunda linha é {maior}')