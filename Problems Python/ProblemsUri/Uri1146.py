x = 1

while x != 0:
    x = int(input())
    for c in range(x):
        if c == x-1:
            print('{}'.format(c+1))
        else:
            print('{}'.format(c+1), end=' ')