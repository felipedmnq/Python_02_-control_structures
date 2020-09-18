# leia o sexo de uma pessoa mas só aceite "M" eou "F", caso esteja errado faça a digitação novamente até um valor correto.
aux = ''
while aux != 'M' and aux != 'F':
    aux = str(input('\033[1;33mDigite seu sexo [M/F]: \033[m')).upper().strip()[0]  # [0] pega apenas a primeira letra.
    if aux != 'M' and aux != 'F':
        print('\033[1;31mDados inválidos, por favor informe seu sexo.\033[m')
if aux == 'F':
    print('\033[1;35mSEXO FEMININO.\033[m')
elif aux == 'M':
    print('\033[1;34mSEXO MASCULINO.\033[m')