# leia nome e preço de varios produtos. usuario escolhe se continua. mostrar:
#A) total gasto na compra. B) quantos produtos custam mais de R$1000. C) nome do produto mais barato.

tot = maior1000 = cont = prodmenor = 0
#prodmenor = 100000000  #GAMBIARRA
prod = ''
while True:
    print('\033[1;33m=' * 30)
    produto = str(input('PRODUTO: '))
    val = float(input('VALOR DO PRODUTO: R$ '))
    cont += 1
    if cont == 1 or val < prodmenor:               #SE FOR O 1º PRODUTO DIGITADO! SERVE PARA ELIMINAR A GAMBIARRA
        prodmenor = val                            # "or" eliminou um bloco igual logo abaixo
        prod = produto
    print('\033[1;33m=' * 30)
#   if val < prodmenor:
#       prodmenor = val
#       prod = produto
    if val >= 1000:
        maior1000 += 1
    tot += val
    c = ' '
    while c not in 'SN':
        c = str(input('DESEJA CONTINUAR? [S/N]: ')).upper().strip()[0]
    if c == 'N':
        break
print('\033[1;33m=' * 30)
print('{:-^30}'.format('FIM DO PROGRAMA'))
print('\033[1;33m=' * 30)
print(f'TOTAL DA COMPRA: R$ {tot:.2f}')
print(f'{maior1000} produtos custaram mais de R$ 1000.00')
print(f'O produto mais barato foi {prod}, que custou R$ {prodmenor:.2f}.')
print('\033[1;33m=' * 30)
