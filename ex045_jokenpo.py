#jogo pedra, papel e tesoura.
# jogar contra o computador

from random import randint
from time import sleep

cpu = int(randint(0,2))
print('\033[1;34m-=-\033[m' * 8)
print('\033[1;34m         JOKEMPO\033[m')
print('\033[1;34m-=-\033[m' * 8)
print('\033[1;34m[0] - PEDRA.\n[1] - PAPEL.\n[2] - TESOURA.\033[m')
player = int(input('\033[1;34mFAÇA SUA JOGADA: \033[m'))
print('\033[1;34m-=-\033[m' * 8)
print('\033[1;33mPlayer: \033[m', player)
print('\033[1;33m     X      \033[m')
print('\033[1;33mCPU :   \033[m', cpu)
print('\033[1;34m-=-\033[m' * 8)
if cpu == player:
    print('\033[1;33mEMPATE\033[m')
elif cpu == 0 and player == 1:
    print('\033[1;33mPAPEL ganha de PEDRA.\nVOCÊ GANHOU!\033[m')
elif cpu == 0 and player == 2:
    print('\033[1;33mPEDRA ganha de TESOURA.\nVOCÊ PERDEU!\033[m')
elif cpu == 1 and player == 0:
    print('\033[1;33mPAPEL ganha de PEDRA.\nVOCÊ PERDEU!\033[m')
elif cpu == 2 and player == 0:
    print('\033[1;33mTESOURA perde de PEDRA.\nVOCÊ GANHOU!\033[m')
elif cpu == 1 and player == 2:
    print('\033[1;33mTESOURA ganha de PAPEL.\nVOCÊ GANHOU!\033[m')
elif cpu == 2 and player == 1:
    print('\033[1;33mTESOURA ganha de PAPEL.\nVOCÊ PERDEU!\033[m')


