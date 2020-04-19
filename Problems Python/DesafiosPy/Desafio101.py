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
    if r >= 18 and r <= 60:
      return ('É obrigatorio votar!')  
    elif r < 16:
        return ('Não pode votar!')
    elif r >= 16 and r < 18 or r >= 60:
        return('Seu voto é opcional!')

ano = int(input('Em qual ano você nasceu? '))
frescura()
print(voto(ano))