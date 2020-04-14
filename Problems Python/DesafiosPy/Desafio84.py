c = "s"
pessoas = list()
dados = list()
contP = 0

while c not in 'Nn':
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite seu peso em Kg: ")))
    pessoas.append(dados[:])
    dados.clear()
    c = str(input("Deseja continuar? [S/N]"))
    contP += 1

print(f"Foram cadastradas {contP} pessoa(s)")
print("As mais pesadas são: ")
for c in pessoas:
    if c[1] >= 80:
        print(f"{c[0]} com {c[1]} Kg")
print("E as mais leves: ")
for c in pessoas:
    if c[1] < 80:
        print(f"{c[0]} com {c[1]} Kg")