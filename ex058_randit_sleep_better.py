# melhorar o ex028 - cpu pensa em numero de 0 a 10, jogador tenta adivinhar até acertar, mostrar no final
#quantos palpites foram necessários.

from random import randint
from time import sleep

cont = 0
cpu = int(randint(0, 10))
player = 435
while cpu != player:
    player = int(input('Tente adivinhar o numero pensado pelo computador entre 0 e 10: '))
    cont += 1
    if player != cpu:
        if player < cpu:
            print('\033[1;31mVOCÊ ERROU!!\033[1;33m TENTE UM NÚMERO MAIOR.\033[m')
        if player > cpu:
            print('\033[1;31mVOCÊ ERROU!!\033[1;33m TENTE UM NÚMERO MENOR.\033[m')
print('\033[1;37mO computador pensou no número {}.'.format(cpu))
print('\033[1;34mVOCÊ ACERTOU!!\033[m')
print('\033[1;33mForam necessárias {} tentativas para você acertar o número.\033[m'.format(cont))