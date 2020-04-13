r = int(input('Digite a razão da progressão: '))
a = int(input('Digite o primeiro termo da progressão: '))
for c in range(1, 11):
    print('O termo é {}'.format(a+(c-1)*r))