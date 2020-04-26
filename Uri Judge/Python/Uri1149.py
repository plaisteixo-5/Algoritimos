total = 0
n = 0
a = int(input())
while n <= 0:
    n = int(input())
for c in range(0,n):
    total += c+a
print('{}'.format(total))