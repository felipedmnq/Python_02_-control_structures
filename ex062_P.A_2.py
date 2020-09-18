print('GERADOR DE P.A.')
print('-=' * 10)
n1 = int(input('1º TERMO DA P.A: '))
r = int(input('RAZÃO DA P.A: '))
t = n1
cont = 1
total = 0
more = 10
while more != 0:
    total += more
    while cont <= total:
        print('{} - '.format(t), end='')
        t += r
        cont += 1
    print('PAUSA')
    more = int(input('MAIS QUANTOS TERMOS DA P.A DESEJA?: '))
print('P.A finalizada, foram mostrados {} termos.'.format(total))