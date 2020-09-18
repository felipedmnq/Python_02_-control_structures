# leia varios numeros, mostre no final a media, maior e menor numeros. o usuario determina se continua ou nao
n = avg = bigger = contn = lower = 0
lim = 'S'
while lim != 'N':
    n = int(input('Digite um valor: '))
    if contn == 1:
        bigger = lower = n
    if n > bigger:
        bigger = n
    if n < lower:
        lower = n
    avg += n
    contn += 1
    lim = str(input('DESEJA CONTINUAR [S/N]?: ')).upper()
print('QUANTIDADE DE NÚMEROS DIGITADOS: {}.\nMÉDIA DOS VALORES: {:.2f}.\nMAIOR VALOR: {}.\nMENOR VALOR: {}.'
      .format(contn, (avg / contn), bigger, lower))
