# def mensagem(algo):
#     print('-'*10)
#     print(algo)
#     print('-'*10)


# mensagem('Funcionou')
# -----------------------------
# def soma(*num): 
#ELE FEZ UMA TUPLA AQUI#
#     sorted(num)
#     print(sorted(num))

# soma(3,4,7,2)
# -----------------------------
# def dobra(*lst):
#     for c in range(0,len(lst)):
#         pos = 0
#         while pos < len(lst[c]):
#             lst[c][pos] *= 2
#             pos += 1

# valores = [6,4,3,34,4]
# valores2 = [1,3,4,5,6]
# dobra(valores,valores2)
# print(valores,valores2)
# -----------------------------
# help(input)
# -----------------------------
# def contador(i,f,p):
#     """
#     i: variável de ínicio da contagem;
#     f: váriável do fim da contagem;
#     p: de quanto em quanto que a contagem será feita.
#     return: não retorna nada
#     """
#     for c in range(i,f,p):
#         print(c)

# contador(0,10,3)
# help(contador)
# -----------------------------
# def somar(a,b,c = 0): -> Aqui quando "c" não for declarado ele vai atribuir 0
#     print(f'A soma é {a+b+c}')
# somar(3,2,5)
# somar(3,2)