# jogue par ou impar. jogo para quando o jogador perder. mostrar total de vitórias.
# digite um valor:
# par ou impar? [P/I]

from random import randint
cont = 0
print('\033[1;32m=' * 30)
print('         PAR OU IMPAR')
print('\033[1;32m=' * 30)
while True:
    cpu = randint(0, 10)
    player = int(input('\033[1;32mDigite um número: '))
    po = ' '
    while po not in 'PI':
        po = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]   # .strip tira os espaços [0] pega apenas a primeira letra
    sum = cpu + player
    if sum % 2 == 0 and po == 'P' or sum % 2 != 0 and po == 'I':
        cont += 1
        print('\033[1;34m=' * 30)
        print(f'CPU = {cpu}\nPlayer = {player}')
        print(f'{cpu} + {player} = {sum}')
        print('VOCÊ VENCEU')
        print('\033[1;34m=' * 30, '\033[m')
    else:
        print('\033[1;31m=' * 30)
        print(f'CPU = {cpu}\nPlayer = {player}')
        print(f'{cpu} + {player} = {sum}')
        print('VOCÊ PERDEU')
        print('\033[1;31m=' * 30)
        break
    print('\033[1;37mVamos jogar novamente!\033[m')
print(f'\033[1;33mTOTAL DE VITÓRIAS: {cont}.')
print('FIM DO JOGO')
