#leia ano de nascimento de 7 pessoas
#mestre quais atingiram a maioridade 21 anos.

from datetime import date
now = date.today().year

s = 0
for c in range(1, 8):
    nasc = int(input("Digite seu ano de nascimento: "))
    if (now - nasc) >= 21:
        s += 1
print('Das {} pessoas cadastradas, {} são maiores de 21 anos.'.format(c, s))
