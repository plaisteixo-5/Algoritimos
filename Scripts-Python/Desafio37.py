num = int(input('Digite um número: '))
escolha = int(input("""Escolha uma das bases para conversão: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
"""))

if(escolha == 1):
    print('O número {} convertido para binário é {}'.format(num,bin(num)))
elif(escolha == 2):
    print('O número {} convertido para octal é {}'.format(num,oct(num)))
else:
    print('O número {} convertido para octal é {}'.format(num,hex(num)))