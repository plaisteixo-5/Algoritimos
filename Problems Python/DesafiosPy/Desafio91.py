from random import randint
from operator import itemgetter
from time import sleep

cont = 1
jogadores = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}
print("Valores sorteados:")
for k,v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(0.5)

jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("Ranking dos Jogadores:")
for k,v in enumerate(jogadores):
    print(f'    {cont}° lugar: {v[0]} com {v[1]}')
    cont += 1