# leia o primeiro termo e a razao de uma PA. mostre os 10 primeiros termos da PA.
# quando acabar, perguntar ao usuario mais quantos termos ele deseja visualizar e mostrar os termos.

n1 = int(input('1º TERMO DA P.A: '))
r = int(input('RAZÃO DA P.A: '))
termo = int(input('QUANTOS TERMOS DA P.A: '))
c = 'S'

print(n1, end=' ')
while c != 'N':
    while n1 <= termo * r:
        n1 += r
        print(n1, end=' ')
    c = str(input('\nDESEJA CONTINUAR [S/N]?: ')).upper()
    if c == 'S':
        termo += int(input('MAIS QUANTOS TERMOS DA P.A DESEJA?: '))
print('FIM')
# este programa não está correto.