flag = 0
x = int(input())
y = int(input())


if y < x:
    a = y
    b = x
else:
    a = x
    b = y
a += 1

while a < b:
    if a % 5 == 2 or a % 5 == 3:
        print(a)
    a += 1