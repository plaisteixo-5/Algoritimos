matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input(f"DIgite um valor para [{c}, {i}]: "))
print('+='*5)
for c in range(0,3):
    for i in range(0,3):
        if i == 2:
            print(f'[{matriz[c][i]}]',end='')
        else:
            print(f'[{matriz[c][i]}]',end=' ')
    print()