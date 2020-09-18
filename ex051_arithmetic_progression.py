# leia o primeiro termo e a razao de uma PA. Mostre os 10 primeiros termos da PA.

a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
print('\033[1;31m=' * 22)
print('\033[1;34m10 TERMOS DE UMA P.A.')
print('\033[1;31m=' * 22)
for c in range(a1, a1 + 10 * r, r):
    print('\033[1;33m', c, end=' -> ')
print('FIM')
