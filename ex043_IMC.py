# ler peso e altura da pessoa e entregar o IMC
# < 18.5 = abaixo do peso
# <18.5 e 25< = peso ideal
# <25 e 30< sobrepeso
# <30 e 40< obesidade
# >40 obesidade morbida

print('\033[1;32m-=-\033[m' * 8)
print('\033[1;32mCALCULADORA IMC.\033[m')
print('\033[1;32m-=-\033[m' * 8)

name = input('\033[1;32mNOME: \033[m')
w = float(input('\033[1;32mPESO (kg): \033[m'))
h = float(input('\033[1;32mALTURA (kg): \033[m'))
imc = w / (h**2)

print('\033[1;32m-=-\033[m' * 8)
print('\033[1;32mNOME: {}.\nPESO (kg): {}.\nALTURA (m): {}.\nIMC: {:.2f}.\033[m'.format(name.upper(), w, h, imc))
print('\033[1;32m-=-\033[m' * 8)

if imc < 18.5:
    print('\033[1;33mBAIXO DO PESO.\033[m')
elif imc >= 18.5 and imc < 25:         # A SEGUNDA PARTE (" AND...") NÃO É NECESSÁRIA NO PYTHON
    print('\033[1;34mPESO IDEAL.\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSOBREPESO.\033[m')
elif imc >= 30 and imc < 40:
    print('\033[1;31mOBESIDADE.\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA.\033[m')

print('\033[1;32m-=-\033[m' * 8)
