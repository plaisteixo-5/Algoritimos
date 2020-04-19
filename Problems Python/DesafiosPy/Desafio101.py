from datetime import datetime
from time import sleep

def frescura():
    print('Análisando sua situação ',end='')
    cont = 0
    while cont < 3:
        print('.',end='',flush=True)
        sleep(0.4)
        cont += 1
    print()

def voto(ano):
    r = datetime.now().year - ano
    if r >= 18:
      return ('É obrigatorio votar!')  
    elif r < 16:
        return ('Não pode votar!')
    else:
        return('Seu voto é opcional!')

ano = int(input('Em qual ano você nasceu? '))
frescura()
print(voto(ano))