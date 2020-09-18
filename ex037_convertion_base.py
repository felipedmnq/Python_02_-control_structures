# leia um numero inteiro e paça p usuario escolher a base de conversão
# 1) binário; 2) octal; 3) hexadecimal.

num = int(input('DIGITE UM NÚMERO INTEIRO: '))

print('\033[1;31m-=-\033[m' * 10)
print('\033[1;33mCONVERSOR DE BASES DECIMAIS\033[m')
print('\033[1;31m-=-\033[m' * 10)
print('\033[1;34mSELECIONE A BASE DE CONVERSÃO: \033[m') #(''') aspas triplas para poder "visualisas" no formato certo o menu.
print('''\033[1;33m                                     
[1] - BINÁRIO.
[2] - OCTAL.
[3] - HEXADECIMAL.\033[m''')
print('\033[1;31m-=-\033[m' * 10)
choice = int(input('\033[1;34mOPÇÃO: \033[m'))

bin = (bin(num)[2:])  # [2:] - inicia na posição 2 (3ª caracter) o texto. (retira os dois primeiros caracteres.
octal = (oct(num)[2:])
hexd = (hex(num)[2:])

if choice == 1:
    print('\033[1;33mVALOR A CONVERTER: {}.\nBINÁRIO: {}\033[m'.format(num, bin))
elif choice == 2:
    print('\033[1;33mVALOR A CONVERTER: {}.\nBINÁRIO: {}\033[m'.format(num, octal))
elif choice == 3:
    print('\033[1;33mVALOR A CONVERTER: {}.\nBINÁRIO: {}\033[m'.format(num, hexd))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA.\033[m')