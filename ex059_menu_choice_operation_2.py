from time import sleep
n1 = int(input('\033[1;32m1º VALOR: \033[m'))
n2 = int(input('\033[1;32m2º VALOR: \033[m'))
option = 0
while option != 5:
    print('''\033[1;33m======MENU DE OPÇÕES=====.
    [1] - SOMAR.
    [2] - MULTIPLICAR.
    [3] - MAIOR.
    [4] - NOVOS NÚMEROS.
    [5] - SAIR.\033[m''')
    print('\033[1;31m=\033[m' * 25)
    option = int(input('\033[1;34mQUAL SUA OPÇÃO?: \033[m'))
    if option == 1:
        print('\033[1;34m{} + {} = {}.\033[m'.format(n1, n2, n1 + n2))
    elif option == 2:
        print('\033[1;34m{} X {} = {}.\033[m'.format(n1, n2, n1 * n2))
    elif option == 3:
        if n1 > n2:
            print('\033[1;34m{} é maior que {}.\033[m'.format(n1, n2))
        elif n2 > n1:
            print('\033[1;34m{} é maior que {}.\033[m'.format(n2, n1))
        else:
            print('\033[1;34m{} é igual a {}.\033[m'.format(n2, n1))
    elif option == 4:
        print('\033[1;33mINFORME OS VALORES NOVAMENTE: ')
        n1 = int(input('\033[1;32m1º VALOR: \033[m'))
        n2 = int(input('\033[1;32m2º VALOR: \033[m'))
    elif option == 5:
        print('\033[1;33mFinalizando...\033[m')
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE!\033[m')
    sleep(2)
print('\033[1;32mOBRIGADO!\033[m')
