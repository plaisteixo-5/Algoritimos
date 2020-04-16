jogador = dict()
partidas = list()

jogador['Nome'] = str(input("Nome Jogador: "))
n = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for i in range(0, n):
    partidas.append(int(input(f'    Digite quantos gols o jogador fez na partida {i+1} ')))
jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = sum(partidas)
print('=-'*30)
print(f'O jogador(a) {jogador["Nome"]} jogou {len(partidas)} partidas.')
for i,k in enumerate(partidas):
    if k == 0:
        print(f'Na {i+1}° partida ele não marcou nenhum gol')
    else:
        print(f'Na {i+1}° partida ele marcou {k} gols')
print('=-'*30)
print(f'Totalizando {jogador["Total de Gols"]} gols')
