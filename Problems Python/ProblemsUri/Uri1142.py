n = int(input())
a = 1
b = 2
c = 3
i = 0


while i < n:
    print('{} {} {} PUM'.format(a,b,c))
    a = 2 + c
    b = a + 1
    c = b + 1
    i += 1