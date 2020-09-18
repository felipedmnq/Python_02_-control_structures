#mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario. interromper o programa
# quando for digitado valor negativo.

while True:
    n = int(input('\033[1;33mDigite um número para saber sua tabuada \033[1;31m[nº negativo encerra o programa]\033['
                  'm\033[1;33m: '))
    if n < 0:
        break
    print('\033[1;34m=' * 20)
    print(f'\033[1;31m    TABUADA DE {n}')
    print('\033[1;34m=' * 20)
    for c in range (0, 11):
        print(f'\033[1;32m{n} X {c} = {n * c}\033[m')
    print('\033[1;34m=' * 20)
print('\033[1;34m=' * 20)
print('\033[1;31m  FIM DO PROGRAMA')
print('\033[1;34m=' * 20)
