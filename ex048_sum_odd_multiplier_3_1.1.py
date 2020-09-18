s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print('{}, '.format(c))
        s += c
        cont += 1
print('A soma dos numeros ímpares multiplos de 3 entre 1 e 500 é: {}.\nForam somados {} números.'.format(s,cont))
