n = int(input())
a = 1
b = 1
c = 1
i = 0

while i < n:
    print('{} {} {}'.format(a,b,c))
    a += 1
    b = a**2
    c = a**3
    i += 1