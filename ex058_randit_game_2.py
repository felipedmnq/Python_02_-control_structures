from random import randint
cpu = int(randint(0, 10))
print('\033[1;33mSou seu computador e acabei de pensar em um número entre 0 e 10.'
      '\nTENTE ADIVINHAR O NÚMERO QUE PENSEI!!!\033[m')
correct = False
choices = 0
while not correct:
    player = int(input('\033[1;34mQual é seu palpite?: \033[m'))
    choices += 1
    if cpu == player:
        correct = True
    else:
        if player < cpu:
            print('\033[1;33mErrou, tente um número maior!!\033[m')
        elif player > cpu:
            print('\033[1;33mErrou, tente um número menor!!\033[m')
print('\033[1;35mGrande garoto!!! ACERTOU !!!\033[m')
print('\033[1;32mForam necessários {} palpites.\033[m'.format(choices))
