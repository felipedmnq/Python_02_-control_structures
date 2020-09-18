#leia o ano de nascimento de um jovem. Informe: se ainda vai se alistar. se esta na hora de se alistar. se ja passou o tempo
# mostrar o tempo que falta ou que passou do prazo.

from datetime import date

name = input('\033[1;31mDigite seu nome: \033[m')
year = int(input('\033[1;31mDigite seu ano de nascimento: \033[m'))
year2 = date.today().year
age = year2 - year
sex = str(input('\033[1;31mQual seu sexo [M/F]?: \033[m'))

if sex == 'M':
    if age < 18:
        print('\033[1;34m{}, AINDA FALTAM {} ANOS PARA SEU ALISTAMENTO! UFFA\033[m'.format(name, (18 - age)))
    elif age > 18:
        print('\033[1;33m{}, JÁ PASSOU DA HORA DE SE ALISTAR! VOCE ESTÁ {} ANOS ATRASADO!\033[m'.format(name, (age - 18)))
    elif age == 18:
        print('\033[1;31m{}, ESTÁ NA HORA DE SE ALISTAR, SE FODEU!\033[m'.format(name))
else:
    print('\033[1;33mO serviço militar é opcional para mulheres.\033[m')
