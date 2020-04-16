alunos = list()
dados = list()
nome = ""
nota1 = 0
nota2 = 0
media = 0
c = "s"

while c not in 'Nn':
    nome  = str(input("Nome: "))
    nota1  = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    media = (nota1+nota2)/2
    dados.append(media)

    alunos.append(dados[:])
    dados.clear()
    media = 0
    c = str(input("Adicionar mais um aluno?[S/N] "))

print('-='*30)
print(f'{"Num.":<6}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i,a in enumerate(alunos):
    print(f'{i:<6}{a[0]:<10}{a[3]:>7.1f}')

while True:
    print('-'*30)
    i = int(input('Deseja ver as notas de algum aluno?(999 caso não): '))
    if i == 999:
        break
    print(f'As notas de {alunos[i][0]} foram {alunos[i][1]} e {alunos[i][2]}')
