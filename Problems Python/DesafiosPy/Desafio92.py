from datetime import datetime

pessoa = dict()

pessoa['Nome'] = str(input("Nome: "))
pessoa['Idade'] = datetime.now().year-int(input("Ano de nascimento: "))
pessoa['CTPS'] = int(input("Carteira de trabalho: "))

if pessoa['CTPS'] != 0:
    pessoa['Ano de Contrato'] = int(input('Em qual ano o contrato foi realizado? '))
    pessoa['Salário'] = float(input('Digite o valor do seu salário: '))
    pessoa['Aposentadoria'] = ((pessoa['Ano de Contrato'] + 35) - datetime.now().year) + pessoa['Idade']
    for i,v in pessoa.items():
        print(f' - {i}: {v}')

else:
    for i,v in pessoa.items():
        if i == 'CTPS':
            print(f' - {i}: Não tem Carteira de Trabalho')
        else:
            print(f' - {i}: {v}')