ex = ''
chaves = []
colchetes = []
parenteses = []
flag = 1

ex = str(input('Digite uma expressão matématica: '))

for c in range(0,len(ex)):
    if ex[c] == '(':
        parenteses.append('(')
    elif ex[c] == '[':
        chaves.append('[')
    elif ex[c] == '{':
        colchetes.append('{')

    elif ex[c] == ')':
        if '(' in parenteses:
            parenteses.pop()
        else:
            print('Expressão inválida')
            flag = 0
            break

    elif ex[c] == ']':
        if '(' in chaves:
            chaves.pop()
        else:
            print('Expressão inválida')
            flag = 0
            break
    
    elif ex[c] == '}':
        if '{' in colchetes:
            colchetes.pop()
        else:
            print('Expressão inválida')
            flag = 0
            break
if flag:
    if not parenteses and not chaves and not colchetes:
            print('Expressão válida')
    else:
        print('Expressão inválida')