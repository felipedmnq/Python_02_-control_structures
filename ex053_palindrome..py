# leia uma frase e informe se é um palindromo desconsiderando os espaços (frase que pode ser lida de tras para frente
# e vice versa.

frs = str(input('Digite uma frase para saber se ela é um PALÍNDROMO: ')).upper()
frs1 = frs.strip().replace(' ', '')
frs2 = frs[::-1].replace(' ', '')   #: = começa no inicio; : = termina no fim; -1 = de traz para frente
if frs1 == frs2:
    print('\033[1;34mA frase "{}" é considerada um PALINDROMO.'.format(frs))
else:
    print('\033[1;31mA frase "{}" NÃO é considerada um PALINDROMO.'.format(frs))

