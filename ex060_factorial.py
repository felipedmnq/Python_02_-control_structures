# leia um numero qualquer e mostre seu fatorial. 5! = 5x4x3x2x1 = 120

cont = 1
fat = 1
n = int(input('Digite o número que deseja fatorar: '))
print(n, end=' ')
cont = n
while cont != 0:
    fat = fat * cont
    cont = cont - 1
    if cont != 0:
        print('X', cont, end=' ')
print('=', fat, end=' ')


