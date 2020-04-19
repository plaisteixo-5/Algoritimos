def fatorial(f,s = 0):
    total = 1
    print(f'{f}! = ',end='')
    while f != 0:
        total *= f
        if s == 1:
            if f == 1:
                print(f'{f} = ',end='')
            else:
                print(f'{f} x ',end='')
        f -= 1
    return total

n = int(input('Qual número você quer saber o fatorial? '))
s = bool(input('Você deseja que seja mostrado o cálculo do fatorial?[0 para não 1 para sim] '))
total = fatorial(n,s)
print(total)