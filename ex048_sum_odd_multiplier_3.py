#calcular a soma dos números multiplos de 3 entre 1 e 500.

s = 0
for c in range(1, 500):
    if c % 3 == 0:
        print(c)
        s = s + c
print('A soma dos multiplos de 3 entre 1 e 500 é: {}.'.format(s))