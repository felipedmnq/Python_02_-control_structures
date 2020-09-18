# leia varios numeros inteiros pelo tecaldo, programa só para com 999. ao final mostre quantos numeros foram
# digitadps e a soma entre eles (desconsiderando o flag "999")

n = sn = contn = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        sn += n
        contn += 1
print('Foram digitados {} números e a soma deles é {}.'.format(contn, sn))
print('FIM')
