print('\033[1;34m=' * 30)
print('{:-^30}'.format('BANCO DO FELIPE'))
print('\033[1;34m=' * 30, '\033[m')
val = int(input('\033[1;32mVALOR A SER SACADO: R$ \033[m'))
total = val
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\033[1;33mTotal de {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\033[1;34m=' * 30, '\033[m')