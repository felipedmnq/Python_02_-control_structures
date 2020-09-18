#calcular valor do produto com relação a condição de pagamento
#a vista (dinheiro ou cheque) 10%
# cartao 5%
#ate 2x normal
#> 2x no cartao 20% juros

print('\033[1;34m{:=^40}\033[m'.format(' LOJAS DA TURMINHA '))  #{:^40} == centralizado em 40 espaços. CENTRALIZADO == ^.
prod = float(input('\033[1;37mVALOR DO PRODUTO: R$ \033[m'))

print('\033[1;35m-=-\033[m' * 7)
print('\033[1;35mOPÇÕES DE PAGAMENTO.\033[m')
print('\033[1;35m-=-\033[m' * 7)

print('\033[1;33mVALOR DO PRODUTO: R$ {:.2f}\033[m'.format(prod))
print('''\033[1;33m
[1] A VISTA NO DINHEIRO (-10%).
[2] A VISTA NO CARTÃO (-5%).[m')
[3] ATÉ 2X NO CARTÃO.')
[4] MAIS QUE 2X NO CARTÃO (20% JUROS).\033[m''')

op = int(input('\033[1;31mDIGITE A OPÇÃO DE PAGAMENTO [1 a 4]: \033[m'))

print('\033[1;34m=\033[m' * 40)

if op == 1:
    print('\033[1;34mA VISTA:\nR$ {:.2f}.\033[m'.format(prod * 0.9))
elif op == 2:
    print('\033[1;32mA VISTA NO CARTÃO:\nR$ {:.2f}.\033[m'.format(prod * 0.95))
elif op == 3:
    print('\033[1;35m2X NO CARTÃO:\nR$ {:.2f} EM 2X DE R$ {:.2f}.'.format(prod, prod / 2))
else:
    parc = int(input('\033[1;31mEM QUANTAS VEZES DESEJA PARCELAR? \033[m'))
    print('\033[1;31m'
          'VALOR TOTAL DA COMPRA: R$ {}.\n{}X DE R$ {:.2f}.'.format(prod, parc, ((prod * 1.2) / parc)))
