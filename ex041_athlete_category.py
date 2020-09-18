# ler ano de nascimento. mostrar sua categoria de acordo com idade
# ate 9 anos: mirin; 9 - 14 anos: infantil; 14 - 19 anos: junior; ate 20 anos: senior; > 20 anos: senior

from datetime import date

name = input('NOME DO ATLETA: ')
nyear = int(input('ANO DE NASCIMENTO: '))
age = date.today().year - nyear

print('ATLETA: {}.'.format(name.upper()))
print('IDADE: {}.'.format(age))

if age <= 9:
    print('CATEGORIA: MIRIN.')
elif age <= 14:
    print('CATEGORIA: INFANTIL.')
elif age <= 19:
    print('CATEGORIA: JUNIOR.')
elif age <= 20:
    print('CATEGORIA: SENIOR.')
else:
    print('CATEGORIA: MASTER.')

