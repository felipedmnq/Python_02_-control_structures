# leia um numero N e mostre os N primeiros termos de uma sequencia de fibonacci.

n1 = 0
n2 = 1
n3 = 0
cont = 3
n = int(input('QUANTOS TERMOS DA SEQUENCIA DE FIBONACCI?: '))
print(n1, n2, end=' ')
while cont <= n:
    cont += 1
    n3 = n1 + n2
    print(n3, end=' ')
    n1 = n2
    n2 = n3
print('FIM')