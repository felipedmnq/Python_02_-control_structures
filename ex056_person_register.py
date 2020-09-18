#leio o nome, idade e sexo de 4 pessoas e mostre:
#media de idade.
#nome do homem mais velho.
#quantas mulheres tem menos de 21 anos.
from datetime import date

year = date.today().year
m = 0
m21 = 0
f = 0
avg = 0
hmv = 0
for c in range(1, 5):
    print('-----{}ª Pessoa-----'.format(c))
    name = str(input('NOME: ')).strip().upper()
    ano = int(input('ANO DE NASCIMENTO: '))
    idade = year - ano
    avg += idade
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    if sexo == ('M'):
        if idade > m:
            m = idade
            hmv = name
    else:
        f += 1
    if sexo == ('F') and idade <= 21:
        m21 += 1
print('\033[1;33mA média de idade das pessoas cadastradas é {} anos.'.format(avg/4))
print('\033[1;34mO homem mais velho é {} e tem {} anos.'.format(hmv, m))
print('\033[1;35mForam cadastradas {} mulheres menores de 21 anos.'.format(m21))
