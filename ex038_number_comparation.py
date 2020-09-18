# escreva dois numeros. Copare numeros. Menor valor, maior valor valores iguais

n1 = float(input('\033[1;33mDIGITE UM NÚMERO QUALQUER: \033[m'))
n2 = float(input('\033[1;31mDIGITE OUTRO NÚMERO QUALQUER: \033[m'))

if n1 == n2:
    print('\033[1;32mVALORES IGUAIS.\033[m')
if n1 > n2:
    print('\033[1;37m{} É MAIOR QUE {}\033[m'.format(n1, n2))
else:
    print('\033[1;36m{} É MAIOR QUE {}.\033[m'.format(n2, n1))
