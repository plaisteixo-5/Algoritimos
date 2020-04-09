frase = str(input('Digite alguma frase: ')).strip()

frase = frase.replace(" ",'')
cont = 0
tamanhoF = len(frase)
print(tamanhoF)


for c in range(0, tamanhoF):
    if frase[c] == frase[(tamanhoF-c)-1]:
        cont += 1
if cont == tamanhoF:
    print('Eh um paçindromo')
else:
    print('Não é um palindromo')