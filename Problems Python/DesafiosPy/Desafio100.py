from random import randint

def somaPar(lista):
    total = 0
    for c in lista:
        if c%2 == 0:
            total += c
    return total

def sorteia(lista):
    cont = 0
    while cont < 5:
        lista.append(randint(0,10))
        cont += 1

lista = list()
sorteia(lista)
total = somaPar(lista)
print(lista)
print(total)