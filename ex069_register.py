# ler idade e sexo de várias pessoas. Perguntar se quer continuar. no final mostrar:
# A) quantos maiores de 18; B) quantos homens; quantas mulheres menores de 20.

m = tot18 = fm = 0
while True:
    age = int(input('IDADE: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if age >= 18:
        tot18 += 1
    if age <= 20 and sex == 'F':
        fm += 1
    if sex == 'M':
        m += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).upper()
    if c == 'N':
        break
print('\033[1;33m=' * 30)
print(f'Foram cadastrados:\nMaiores de 18 anos: {tot18} .\nHomens: {m}.\nMulheres menores de 20 anos: {fm}.')
print('\033[1;33m=' * 30)
print('OBRIGADO.')
print('\033[1;33m=' * 30)
