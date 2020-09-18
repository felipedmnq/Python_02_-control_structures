frase = str(input('Digite uma frase: ')).upper().strip()
words = frase.split()
tgdr = ''.join(words)   #junta a frase sem os espaços. (''). pode juntar tudo com o que quiser. ex: * no lugar de ''.
bckwrds = ''
for letter in range(len(tgdr) - 1, -1, -1):  #len(tgdr - 1) = pega a ultima letra; -1 = até a 1ª letra; -1 = anda passo -1 (traz pra frente)
    bckwrds += tgdr[letter]
if bckwrds == tgdr:
    print('\033[1;34mA frase "{}" é considerada um PALÍNDROMO.'.format(frase))
else:
    print('\033[1;31mA frase "{}" NÃO é considerada um PALÍNDROMO.'.format(frase))