mediaIdade = 0
idadeH = 0
nomeVelho = ''
contM = 0

for i in range (0,4):
    print('---- {}ª Pessoa ----'.format(i+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()

    if i == 0 and sexo in 'Mm':
        nomeVelho = nome
        idadeH = idade
    if sexo in 'Mm' and idade > idadeH:
        idadeH = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        contM += 1

    mediaIdade += idade


print('A média de idade do grupo é de {} anos'.format(mediaIdade/4))
print('O homem mais velho se chama {} e sua idade é de {} anos'.format(nomeVelho,idadeH))
print('Tem {} mulheres com menos de 20 anos no grupo'.format(contM))