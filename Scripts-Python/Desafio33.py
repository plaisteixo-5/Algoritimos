n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o primeiro número: '))
n3 = int(input('Digite o primeiro número: '))

if(n1 > n2):
    if(n1 > n3):
        if(n2 > n3):
            print('O maior número é {} e o menor é {}'.format(n1,n3))
        else:
            print('O maior número é {} e o menor é {}'.format(n1,n2))
    else:
        print('O maior número é {} e o menor é {}'.format(n3,n2))
else:
    if(n2 > n3):
        if(n3 > n1):
            print('O maior número é {} e o menor é {}'.format(n2,n1))
        else:
            print('O maior número é {} e o menor é {}'.format(n2,n3))
    else:
        if(n2 > n1):
            print('O maior número é {} e o menor é {}'.format(n3,n1))
        else:
            print('O maior número é {} e o menor é {}'.format(n3,n2))
