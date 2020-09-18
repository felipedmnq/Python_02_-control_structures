sex = str(input('\033[1;33mInforme seu sexo [M/F]: \033[m')).upper().strip()[0]
while sex not in 'MmFf':
    sex = str(input('\033[1;31mDados inválidos! Por favor, informe seu sexo [M/F]: \033[m')).upper().strip()[0]
if sex == 'F':
    print('\033[1;35mSEXO FEMININO REGISTRADO.\033[m')
elif sex == 'M':
    print('\033[1;34mSEXO MASCULINO REGISTRADO.\033[m')