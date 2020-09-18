# repetir ex035. verificar se pode formar triangulo, caso sim, qual modelo? eqilatero, isoceles, escaleno.

print('\033[1;33m-=-\033[m' * 11)
print('\033[1;34mALISADOR DE TRIÂNGULOS\033[m')
print('\033[1;33m-=-\033[m' * 11)

r1 = int(input('\033[1;35mCOMPRIMENRO DA RETA 01: \033[m'))
r2 = int(input('\033[1;35mCOMPRIMENRO DA RETA 02: \033[m'))
r3 = int(input('\033[1;35mCOMPRIMENRO DA RETA 03: \033[m'))

print('\033[1;33m-=-\033[m' * 11)

print('\033[1;36mRETAS: \nR1: {}.\nR2: {}.\nR3: {}.\033[m'.format(r1, r2, r3))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('\033[1;33m-=-\033[m' * 11)
    print('\033[1;34mPODE FORMAR UM TRIÂNGULO \033[m', end='') # TRAZ O PRINT DO IF SECUNDARIO PARA A MESMA LINHA DO IF PRINCIPAL
    if r1 == r2 and r2 == r3:
        print('\033[1;34mEQUILÁTERO.\033[m')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('\033[1;34mISÓCELES.\033[m')
    else:                                          # O ELSE COMPORTA: R1 != R2 != R3, OU R1 != R2 AND R2 != R3 AND R3 != R1.
        print('\033[1;34mESCALENO.\033[m')
else:
    print('\033[1;33m-=-\033[m' * 11)
    print('\033[1;31mIMPOSSÍVEL FORMAR UM TRIÂNGULO.\033[m')


print('\033[1;33m-=-\033[m' * 11)

