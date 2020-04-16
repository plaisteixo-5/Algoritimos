jogador = dict()
partidas = list()
lista = list()
c = 'S'
C = 0

while c not in 'Nn':
    print('=-'*30)
    jogador['Nome'] = str(input("Nome Jogador: "))
    n = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for i in range(0, n):
        partidas.append(int(input(f'    Digite quantos gols o jogador fez na partida {i+1} ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        c = str(input('Deseja continuar?[S/N] '))
        if c not in 'SsNn':
            print('Caractere inválido. Digite novamente S ou N.')
        else:
            break

print(lista)

print('-'*50)
print('# ',end='')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
print('-'*50)
for c,i in enumerate(lista):
    print(f'{c+1}',end=' ')
    for v in i.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*50)
while True:
    C = int(input('Qual jogador você deseja ver detalhes? '))-1
    if C == 998:
        break
    elif C >= len(lista):
        print('Valor inválido. Tente novamente.')
    else:
        print(f'=== O LEVANTAMENTO DO JOGADOR {lista[C]["Nome"]} ===')
        for i,g in enumerate(lista[C]["Gols"]):
            if g == 0:
                print(f'{lista[C]["Nome"]} não marcou nenhum gol na partida {i+1}')    
            else:
                print(f'    =>No jogo {i+1} o jogador fez {g} gols.')
        print('-'*50)
print('-'*50)
print(f'{"Obrigado":^50}')