aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    print(f'O aluno {aluno["nome"]} teve média igual à {aluno["média"]}')
    print(f'A situação de {aluno["nome"]} é de: Aprovado.')
else:
    print(f'O aluno {aluno["nome"]} teve média igual à {aluno["média"]}')
    print(f'A situação de {aluno["nome"]} é de: Reprovado.')