# leia dois valores e apresente um menu com as seguintes opções: 1 - somar; 22 - multiplicar; 3 - maior;
# 4 - novos numeros; 5 - novos numeros

end = 'S'
aux = 7
while aux != 5 and end == 'S':
    n1 = int(input('\033[1;32m    Digite o 1º valor: '))
    n2 = int(input('    Digite o 2º valor: '))
    aux = int(input('''
    \033[1;31m=====MENU DE OPÇÕES=====\033[m
    \033[1;33m[1] - SOMAR.
    [2] - MULTIPLICAR.
    [3] - MAIOR.
    [4] - NOVOS NÚMEROS.
    [5] - SAIR.\033[m
    \033[1;31m========================\033[m
    \033[1;33mOPÇÃO: \033[m'''))
    if aux == 1:
        print('\033[1;34m    {} + {} = {}.\033[m'.format(n1, n2, n1 + n2))
        end = str(input('\033[1;32m    Deseja continuar [S/N]: \033[m')).upper()
    elif aux == 2:
        print('\033[1;34m    {} X {} = {}.\033[m'.format(n1, n2, n1 * n2))
        end = str(input('\033[1;32m    Deseja continuar [S/N]: \033[m')).upper()
    elif aux == 3:
        if n1 > n2:
            print('\033[1;34m    O maior número entre {} e {} é {}.'.format(n1, n2, n1))
        else:
            print('\033[1;34m    O maior número entre {} e {} é {}.'.format(n1, n2, n2))
        end = str(input('\033[1;32m    Deseja continuar [S/N]: \033[m')).upper()
    elif aux == 4:
        continue
print('\033[1;32m    Obrigado.\033[m')
