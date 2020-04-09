n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
din = n1 // n2
print('A soma é {}, o produto é {}, a divisao é {:.5f}'.format(s, m, d), end=' ')
print('A divisão inteira é{} e a exponencial é{}'.format(din, e))