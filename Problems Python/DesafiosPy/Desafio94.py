pessoa = dict()
grupo = list()
c = "S"
mediaG = 0

while c not in 'Nn':
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo:[M/F] ')).upper()
        if pessoa['sexo'] not in 'MmFf':
            print('Sexo inválido. Digite M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Digite a idade: '))
    mediaG += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        c = str(input('Deseja adicionar mais alguém?[S/N] '))
        if c not in 'SsNn':
            print('Caractere inválido. Utilize S ou N.')
        else:
            break
mediaG = mediaG/len(grupo)
print('=-'*10,'-='*10)
print(f'Foram cadastradas {len(grupo)} pessoas.')
print(f'A média de idade do grupo é de {mediaG:.2f}')
print('As mulheres cadastradas foram: ')
for c in grupo:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}')
print('=-'*10,'-='*10)
for c in grupo:
    if c['idade'] > mediaG:
        print(f'O(A) {c["nome"]} tem {c["idade"]}, logo está acima da média')