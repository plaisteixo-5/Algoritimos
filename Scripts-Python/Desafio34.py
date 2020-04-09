s = float(input('Informe seu salário: '))
if(s > 1250):
    print('Seu salário irá de {:.2f} para {:.2f}'.format(s,(s*0.1)+s))
else:
    print('Seu salário irá de {:.2f} para {:.2f}'.format(s,(s*0.15)+s))