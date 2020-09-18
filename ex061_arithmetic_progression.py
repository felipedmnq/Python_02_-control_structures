# leia o primeiro termo e a razao de uma PA. mostre os 10 primeiros termos da PA.

n1 = int(input('Digite o 1º termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
termos = int(input('Digite quantos termos da P.A deseja: '))

print(n1, end=' ')
while n1 <= (termos - 2) * r:
    n1 += r
    print(n1, end=' ')
print('FIM')
