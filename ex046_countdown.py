#faça um programa que mostre uma contagem regressiva para estourar fogos de artificio, com pausa de 1 segundo
#entre elas.
from time import sleep
for c in range(10, 0, -1):
    print('\033[1;31m',c, '...')
    sleep(1)
print('\033[1;31mBOOOOOOMMMMM!!!!!\033[m')
