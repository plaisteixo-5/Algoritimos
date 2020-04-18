from time import sleep

def printaLinha():
    print('=-'*20)

def apresenta():
    printaLinha()
    print('Contagem de 1 até 10 de 1 em 1: ')
    for c in range(1,11):
        print(c, end=' ')
    sleep(0.4)
    print()
    printaLinha()
    print('Contagem de 10 até 0 de 2 em 2: ')
    for c in range(10,-1,-2):
        print(c)
        sleep(0.4)
    print()
    printaLinha()

def contador(i,f,p):
    if i > f:
        if p > 0:
            p = -p
        elif p == 0:
            p = -1
        for c in range(i,f-1,p):
            print(c)
            sleep(0.4)    
    else:
        if p == 0:
            p = 1
        for c in range(i,f+1,p):
            print(c)
            sleep(0.4)

apresenta()

print('Agora é sua vez')
i = int(input('Digite onde começará a contagem: '))
f = int(input('Digite aonde terminará a contagem: '))
p = int(input('Digite de quanto em quanto a contagem será feita: '))
contador(i,f,p)