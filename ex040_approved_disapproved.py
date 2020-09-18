# leia duas notas de um aluno e mostre a media. mostrar se aprovado (>7), recuperação (5 e 6.9) ou reprovado (< 5)

std = input('ALUNO: ').upper()
n1 = float(input('NOTA 1º SEMESTRE: '))
n2 = float(input('NOTA 2 º SEMESTRE: '))
avg = (n1 + n2) / 2

print('\033[1;33m    ESCOLA DA TURMINHA DO BURACO.\033[m')
print('\033[1;33m-\033[m' * 33)
print('\033[1;33mALUNO: {}.\033[m'.format(std))
print('\033[1;33mNOTA 1º SEMESTRE: {}\033[m'.format(n1))
print('\033[1;33mNOTA 2º SEMESTRE: {}\033[m'.format(n2))
print('\033[1;33mMÉDIA: {}\033[m'.format(avg))
print('\033[1;33m-\033[m' * 33)

if avg >= 7:
    print('\033[1;34mALUNO APROVADO!\033[m')
elif 7 > avg >= 5:                                  #avg >= 5 and avg < 7:
    print('\033[1;33mALUNO EM RECUPERAÇÃO.\033[m')
elif avg < 5:
    print('\033[1;31mALUNO REPROVADO.\033[m')
