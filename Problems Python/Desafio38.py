from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
if atual - nascimento > 18:
    print('Você está atrasado {} ano para se alistar'.format((atual-nascimento)-18))
elif atual - nascimento < 18:
    print('Você tem que se alistar daqui {} ano'.format(((atual-nascimento)-18)*(-1)))
else:
    print('Está no momento de se alistar')
