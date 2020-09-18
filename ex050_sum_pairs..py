# leia 6 numeros inteiros e mostre a soma dos pares, Os valores impares digitados devem ser desconsiderados.

sp = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        sp += num
        cont += 1
print('Foram digitados {} números pares e a soma deles é: {}.'.format(cont, sp))
