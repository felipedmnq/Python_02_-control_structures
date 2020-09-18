from random import randint
from time import sleep

plays = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0,2)

print('''\033[1;34mOPÇÕES DE JOGADAS:
[0] - PEDRA.
[1] - PAPEL.
[2] - TESOURA.\033[m''')

player = int(input('\033[1;33mSUA JOGADA: \033[m'))

print('\033[36m=\033[m' * 20)

print('\033[1;35mJO...')
sleep(1)
print('\033[1;35mKEN...')
sleep(1)
print('\033[1;35mPÔ!!!')
sleep(1)

print('\033[36m=\033[m' * 20)
print('\033[1;31mCOMPUTADOR: {}.'.format(plays[cpu]))
print('\033[1;32mJOGADOR: {}.'.format(plays[player]))
print('\033[36m=\033[m' * 20)

if cpu == player:
    print('\033[1;36mEMPATE.\033[m')
elif cpu == 0: #pedra
    if player == 1:
        print('\033[1;32mJOGADOR GANHOU.\033[m')
    elif player == 2:
        print('\033[1;31mCOMPUTADOR GANHOU.\033[m')
elif cpu == 1:  #papel
    if player == 0:
        print('\033[1;31mCOMPUTADOR GANHOU.\033[m')
    elif player == 2:
        print('\033[1;32mJOGADOR GANHOU.\033[m')
elif cpu == 2:  # tesoura
    if player == 0:
        print('\033[1;32mJOGADOR GANHOU.\033[m')
    elif player == 1:
        print('\033[1;31mCOMPUTADOR GANHOU.\033[m')
