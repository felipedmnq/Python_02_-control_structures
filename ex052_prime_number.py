#leia um numero inteiro e informe se ele é primo.

n = int(input('Digite um número inteiro para saber se ele é primo: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;34m', c, '\033[m', end='/')
        s += 1
    else:
        print('\033[1;31m', c, '\033[m', end='/')
if s == 2:
    print('\n\033[1;34m O número {} é PRIMO.\033[m'.format(n))
else:
    print('\n\033[1;31m O número {} NÃO É PRIMO.\033[m'.format(n))
