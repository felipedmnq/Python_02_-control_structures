# simular funcionamento de um caixa eletronico. perguntar qual o valor a ser sacado (numero inteiro).
# programa informa quantas cédulas de cada valor serão entregues (cédulas: R$50, R$20, R$10 e R$1).

print('\033[1;34m=' * 30)
print('{:-^30}'.format('BANCO DO FELIPE'))
print('\033[1;34m=' * 30, '\033[m')
val = int(input('\033[1;32mVALOR A SER SACADO: R$ \033[m'))
print('\033[1;34m=' * 30, '\033[m')
print(f'\033[1;31mVALOR A SACAR: R$ {val}')
ced = val // 50
resto = val % 50
if ced > 0:
    print(f'Total de {ced} cédulas de R$50.')
ced = resto // 20
resto %= 20
if ced > 0:
    print(f'Total de {ced} cédulas de R$20.')
ced = resto // 10
resto %= 10
if ced > 0:
    print(f'Total de {ced} cédulas de R$10.')
ced = resto // 1
if ced > 0:
    print(f'Total de {ced} cédulas de R$1.')
print('\033[1;34m=' * 30, '\033[m')
