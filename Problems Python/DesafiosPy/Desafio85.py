numeros = [[],[]]
n = 0

for c in range(0,7):
    n = int(input(f"Digite o número {c+1}"))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'{numeros}')