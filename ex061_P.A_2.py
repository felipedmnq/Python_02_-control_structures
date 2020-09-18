print('GERADOR DE P.A.')
print('-=' * 10)
n1 = int(input('1º TERMO DA P.A: '))
r = int(input('RAZÃO DA P.A: '))
t = n1
cont = 1
while cont <= 10:
    print('{} - '.format(t), end='')
    t += r
    cont += 1
print('FIM.')
