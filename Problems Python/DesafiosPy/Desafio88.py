from random import randint
from time import sleep

cont = 0
lista = list()
jogos = list()
tot = 0

print('-'*20)
print('      MEGA SENA       ')
print('-'*20)
n = int(input("Quantos jogos você deseja receber?\n"))

while tot < n:
    cont = 0
    while True:
        num  = randint(1,60)
        if num not in jogos and num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(3*'-=', f'Sorteando {n} jogos', 3*'-=')
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1.2)
print(5*'=-','BOA SORTEEE ^.^*',5*'=-')