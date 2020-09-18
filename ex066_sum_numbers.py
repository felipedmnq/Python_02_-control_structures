# leia vários números. Parar em 999. mostrar quantos numeros digitados e a soma.
s = cont = 0
while True:
    n = int(input('\033[1;34mDigite um valor \033[1;31m[Digite 999 para parar]\033[m: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'\033[1;33mForam somados {cont} números, totalizando: {s}.')
