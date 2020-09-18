# aprovar um emprestimo bancário para compra de casa. Perguntar: valor da casa; valor do salario; quantos anos vai pagar
# Calcular: valor da prestação mensal (não pode exceder 30% da renda - senao negado).

print('\033[1;31m-------BANCO SE FODEU!-------\033[m')

name = input('\033[1;31mNOME: \033[m')
h = float(input('\033[1;31mVALOR DO EMPRESTIMO: R$ \033[m'))
s = float(input('\033[1;31mSALÁRIO: R$ \033[m'))
pz = float(input('\033[1;31mPRAZO PARA PAGAMENTO (anos): \033[m'))

prest = (h / (pz * 12))

if (prest <= (s * 0.3)):
    print('\033[1;34mEMPRÉSTIMO APROVADO!\nNOME DO CLIENTE: {}\nVALOR DO EMPRESTIMO: R$ {:.2f}\nPRAZO PARA PAGAMENTO: {} MESES'
          '\nVALOR DA PRESTAÇÃO: R$ {:.2f}\033[m'.format(name, h, (pz * 12), prest))
else:
    print('\033[1;31mEMPRESTIMO REPROVADO!\nVALOR DA PRESTAÇÃO SUPERIOR A 30% DO SALÁRIO.\033[m')

