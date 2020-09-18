#refazer o ex009 - o usuario escolhe o numero da tabuada.

n1 = int(input('\033[1;31mDigite um numero para saber sua tabuada: \033[m'))
print('\033[1;36m=\033[m' * 20)
print('\033[1;34m   TABUADA DE ', n1, '\033[m')
print('\033[1;36m=\033[m' * 20)
for c in range(0, 11):
    print('\033[1;33m', n1, ' X ', c, ' = ', n1 * c, '\033[m')
print('\033[1;36m=\033[m' * 20)

